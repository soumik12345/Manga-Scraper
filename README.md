# Manga Scraper

A simple tool to download Manga and create Chapter-wise PDFs easier to read.

1. Install the latest version of Firefox.

2. Download Gecko Driver for your respective platform.

3. `git clone https://github.com/soumik12345/Manga-Scraper`

4. `cd Manga-Scraper`

5. `python3 -m pip install -r requirements.txt`

6. `python3 main.py` or use the [Notebook](./Download.ipynb).

The CLI will guide you for the rest.

**Note:**

1. The code I have written has been tested on Windows, Linux and MacOS. It seems to be working flawlessly on Mac and
Linux but has a few issues on Windows, especially the `pyautogui` operations.

2. The Manga that are being downloaded are all property of their respective creators. I don't own then in anyway.

3. Manganelo, the site that is being scraped might change their code or page structures in future. I will try my best to
support the application, although I don't give any guarantee.

4. I would, sometimes in future attempt to write a version of the application that runs in Headless mode.

5. If you find some bug in the application, or you think that Manganelo has updated their site, please raise a Pull Request. 
I would address them as per my bandwidth.

6. This application was initially written to collect data for a research project in Computer Vision. However, I soon 
discovered that reading Manga on Kindle is a really awesome experience. Hence, I added the PDF compilation option.

<figure>
  <img src="./assets/sample.jpeg" alt="">
  <figcaption>A sample panel from <strong>Yakusoku No Neverland</strong> on my Kindle</figcaption>
</figure><br><br>

**Enjoy!!!**