# [VisiData](https://visidata.org) plugin for [Ibis](https://ibis-project.org)

Query various database backends without loading the entire database.

## Install

1. Clone the repo:

    git clone https://github.com/saulpw/vdibis.git

2. Install the dependencies (`ibis-framework`):

    pip install -r vdibis/requirements.txt

3. Manually install and load the plugin:

    mkdir -p ~/.visidata/plugins
    ln -s `pwd`/vdibis/vdibis ~/.visidata/plugins
    echo 'import plugins.vdibis' >> ~/.visidatarc

## Usage

    vd -f ibis foo.duckdb

## implemented

- `v` to cycle the sidebar between the generated SQL, the Ibis expression, the Substrait, and no sidebar
- `Shift+F` frequency table
  - Enter to select one value
- hide column
- zM unfurl-col
- set column types
- rename col
- aggregation (name must be function on Ibis column expr; e.g. use `mean`, `avg` is not available)
- sort
- `,` to select rows
- `gt` to toggle selection
- `"` to filter selection
- `&` to join

## Notes

- the SQL/sidebar expression shows what would be executed during reload, not necessarily what the current view is.
  - For example, opening a table through Ibis only loads the first 10,000 rows.  Sorting the table adds an `ORDER BY` clause to the SQL, but only sorts those first 10,000 rows within VisiData.  To re-run the query including the new ORDER BY clause, use `Ctrl+R` to reload the sheet.
