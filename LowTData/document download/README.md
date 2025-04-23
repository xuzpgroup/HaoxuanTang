1. Run the **"elsevier_xml_download.py"** script to download XML-format articles from Elsevier. Run the **"html_download.py"** script to download HTML-format articles from Springer and MDPI. Run the **"html_download_selenium.py"** script to download HTML-format articles from Wiley (requires Google Chrome browser).

2. Run the **"xml_parse_struct_table.py"** script to extract paragraph and table data from the downloaded XML articles from Elsevier.

3. Run the **"html_paser_struct_table_mdpi_wiley.py"** script to extract paragraph and table data from the downloaded HTML articles from Wiley and MDPI.

4. For Springer, a special process is required: first, use **"html_download_table_springer.py"** to download tables from Springer articles; then, use **"html_parse_struct_table_springer.py"** to extract paragraph and table data from the downloaded Springer HTML articles.
