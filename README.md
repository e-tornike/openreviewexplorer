<!-- This template is adapated from https://github.com/othneildrew/Best-README-Template -->

[![Issues][issues-shield]][issues-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">OpenReview Explorer Plus</h3>

  <p align="center">
    An explorer for OpenReview papers.
    <br />
    <br />
    <a href="https://openreviewexplorerplus.onrender.com/">View Demo</a>
    ·
    <a href="https://github.com/e-tornike/openreviewexplorer/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/e-tornike/openreviewexplorer/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://openreviewexplorerplus.onrender.com/)

This is a simple explorer for OpenReview papers. It is inspired by the [Open Review Explorer](https://horace.io/OpenReviewExplorer/#) from [Chillee](https://github.com/Chillee), but has a few unique features on top:

- TL;DR summaries are generated using [BART](https://huggingface.co/facebook/bart-large-cnn)
- Many more venues are included (e.g., NeurIPS, ACL, AAAI), and in total over 28k papers

The interface allows you to search across titles/TL;DRs/keywords and list up to 100 elements at once, 

<!-- GETTING STARTED -->
## Getting Started

Once you have installed all dependencies and started the web app, you can navigate to [http://localhost:8000](http://localhost:8000).

### Prerequisites

* Install [python](https://www.python.org/downloads/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/e-tornike/openreviewexplorer.git
   ```
2. Create and activate a virtual environment
   ```sh
   python3 -m venv venv
   source /venv/bin/activate
   ```
3. Install python packages
   ```sh
   pip install -r requirements.txt
   ```


<!-- USAGE EXAMPLES -->
## Usage

Run the application on a specified port (e.g., port 8000) and navigate to [http://localhost:5000](http://localhost:5000):
```sh
  flask --app app run
```

<!-- LICENSE -->
## License

MIT license. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Tornike Tsereteli - tsereteli.tornike@gmail.com


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[issues-shield]: https://img.shields.io/github/issues/e-tornike/openreviewexplorer.svg?style=for-the-badge
[issues-url]: https://github.com/e-tornike/openreviewexplorer/issues
[license-shield]: https://img.shields.io/github/license/e-tornike/openreviewexplorer.svg?style=for-the-badge
[license-url]: https://github.com/e-tornike/openreviewexplorer/blob/master/LICENSE
[product-screenshot]: images/screenshot.png
