# How to add your photos

Drop files directly in this folder (no subfolders) using these exact
prefixes, numbered 1 up to 5. Any of .jpg, .jpeg, .png, .webp works,
and you can mix formats. You don't need all 5 -- 1 is fine, so is 3.

After adding files, rebuild: `cd ../_build && python3 build.py`
Every page that shows that project (or your profile) picks up the
real photo automatically -- no code or data file edits needed.

## Profile photos (hero + About page)
    Elice_1.jpg   <- used on the homepage hero
    Elice_2.jpg   <- used on the About page (falls back to Elice_1 if missing)
    Elice_3.jpg through Elice_5.jpg are detected but not placed yet --
    ask Claude to wire one in if you want a third spot (e.g. footer).

## Project screenshots (case study galleries)
    TrustLake_1.jpg       through TrustLake_5.jpg
    SalesPipeline_1.jpg   through SalesPipeline_5.jpg
    GlowMart_1.jpg        through GlowMart_5.jpg
    Airbnb_1.jpg          through Airbnb_5.jpg
    GoldenWok_1.jpg       through GoldenWok_5.jpg
    DigitalWallet_1.jpg   through DigitalWallet_5.jpg
    CustomerChurn_1.jpg   through CustomerChurn_5.jpg
    Ecommerce_1.jpg       through Ecommerce_5.jpg
    DevSurvey_1.jpg       through DevSurvey_5.jpg
    InventoryLog_1.jpg    through InventoryLog_5.jpg
    DataCleaningEDA_1.jpg through DataCleaningEDA_5.jpg

What happens once you add them:
- The project's card (on the homepage, /work.html, and capability
  filter results) shows _1 as its thumbnail instead of the plain icon.
- The case-study page shows a full scrollable gallery of every image
  you added for that project, in order.
- These prefixes are defined in ../_build/projects_data.py as each
  project's "imagePrefix" -- if you rename a project's slug later,
  update the prefix there too (or just keep using the same prefix,
  it doesn't have to match the title exactly).

## GlowMart documentation images (extra names, used on its two doc pages)
These are separate from the GlowMart_1..5 gallery. Rename your existing
files like this:

    Overview.png   -> GlowMart_1.png            (gallery + Business page)
    Deepdive.png   -> GlowMart_2.png            (gallery + Business page)
    Customer.png   -> GlowMart_3.png            (gallery + Business page)
    Model.png      -> GlowMart_Model.png        (Technical page, data model)
    Table1.png     -> GlowMart_Table_Sales.png
    Table4.png     -> GlowMart_Table_Customer.png
    Table2.png     -> GlowMart_Table_Product.png
    Table3.png     -> GlowMart_Table_Date.png

Until a file exists, its spot shows a dashed placeholder naming the file.

## ER Patient Analysis
    ERPatient_1.png   the report page. A cropped copy of your screenshot is
                      already included. Replace it with a clean export any
                      time, using the same file name.
