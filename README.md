# Web Application Development homework
This repository contains source codes of WAD's homework

## Homework 1
My personal page contains:
* The header with navigation panel and site logo;
* Paragraph with personal information;
* Table with course technologies and explanation why they'll be useful for me;
* Footer with owner name and current website version.

In the Flask version, HTML pages are rendered by Jinja templates. There are 2 HTML files:
* base.html – used as a basement for all pages and include header and footer and other configuration information like reference to CSS file;
* index.html – the content of /profile page;

While reaching the default address of the website, the Flask will redirect this request to /profile page.

Footer's information is stored in project_info directory as a YAML file and then is parsed by Python.
