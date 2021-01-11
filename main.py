import os
from mangafetcher.manganelo_manager import (
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
    print('{} -> {}'.format(result.title, result.url))

manga_url = input('Enter URL of the Manga: ')
chapters = ChapterManager.get_chapter_links(chapter_url=manga_url.strip())
chapters = chapters[::-1]
print('Total Number of Chapters: {}'.format(len(chapters)))


make_directory('dump')

start_index = int(input('Enter the number of the book to start downloading from: '))
end_index = int(input('Enter the number of the book to start downloading from: '))

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
    downloader = ChapterDownloader(dump_path=os.getcwd() + '/dump/')
    downloader.download_images(chapters[index].url)
    print('Compiling into PDF')

    print()

    PDFCreator.create_pdf(
        image_dump_dir='./dump/',
        pdf_location=pdf_location + '/{}.pdf'.format(chapters[index].title)
    )