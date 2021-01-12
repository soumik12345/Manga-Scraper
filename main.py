import os
from mangafetcher import (
    SearchEngine, ChapterManager,
    ChapterDownloader, PDFCreator
)
from mangafetcher.utils import (
    make_directory, remove_directory
)


query_string = input('Enter the manga you want: ')
search_engine = SearchEngine(query=query_string.strip())
results = search_engine.results()
for result in results:
    try: print('{} -> {}'.format(result.title, result.url))
    except: pass

manga_url = input('Enter URL of the Manga: ')
chapters = ChapterManager.get_chapter_links(chapter_url=manga_url.strip())
chapters = chapters[::-1]
print('Total Number of Chapters: {}'.format(len(chapters)))


make_directory('dump')

start_index = int(input('Enter the number of the book to start downloading from: '))
end_index = int(input('Enter the number of the book to start downloading from: '))

gecko_driver_path = input('Enter Geckodriver Path: ')
compile_to_pdf = input('Compile to PDF???[y/n] ').lower()
compile_to_pdf = True if compile_to_pdf == 'y' else False

remove_directory('./dump/')
make_directory('pdf_dump')
pdf_location = './pdf_dump'

for index in range(start_index - 1, end_index - 1):

    remove_directory('./dump/')
    make_directory('dump')

    print(
        'Downloading Chapter {} from {}...'.format(
            chapters[index].title, chapters[index].url
        )
    )
    downloader = ChapterDownloader(
        executable_path=gecko_driver_path,
        dump_path='C:\\Workspace\\Manga-Scraper\\dump'
    )
    downloader.download_images(chapters[index].url)

    if compile_to_pdf:
        print('Compiling into PDF')
        PDFCreator.create_pdf(
            image_dump_dir='./dump/',
            pdf_location='test.pdf'
            # pdf_location=pdf_location + '/' + chapters[index].title + '.pdf'
        )

remove_directory('./dump/')
