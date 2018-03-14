
Restfulpy Boilerplate
=====


Setting up development Environment on Linux
----------------------------------

### Installing Dependencies

    $ sudo apt-get install libass-dev libpq-dev postgresql \
        build-essential redis-server redis-tools

### Setup Python environment

    $ sudo apt-get install python3-pip python3-dev
    $ sudo pip3 install virtualenvwrapper
    $ echo "export VIRTUALENVWRAPPER_PYTHON=`which python3.6`" >> ~/.bashrc
    $ echo "alias v.activate=\"source $(which virtualenvwrapper.sh)\"" >> ~/.bashrc
    $ source ~/.bashrc
    $ v.activate
    $ mkvirtualenv --python=$(which python3.6) --no-site-packages restfulpy-boilerplate

#### Activating virtual environment
    
    $ workon restfulpy-boilerplate

#### Upgrade pip, setuptools and wheel to the latest version

    $ pip install -U pip setuptools wheel
  
### Installing Project (edit mode)

So, your changes will affect instantly on the installed version

#### nanohttp

    $ cd /path/to/workspace
    $ git clone git@github.com:Carrene/nanohttp.git
    $ cd nanohttp
    $ pip install -e .
    
#### restfulpy
    
    $ cd /path/to/workspace
    $ git clone git@github.com:Carrene/restfulpy.git
    $ cd restfulpy
    $ pip install -e .

#### restfulpy-boilerplate
    
    $ cd /path/to/workspace
    $ git clone git@github.com:Carrene/restfulpy-boilerplate.git
    $ cd restfulpy-boilerplate
    $ pip install -e .
    
#### Enabling the bash auto completion for restfulpy-boilerplate

    $ echo "eval \"\$(register-python-argcomplete restfulpy-boilerplate)\"" >> $VIRTUAL_ENV/bin/postactivate    
    $ deactivate && workon restfulpy-boilerplate
    
### Setup Database

#### Configuration

Create a file named `~/.config/restfulpy-boilerplate.yml`

```yaml
db:
  url: postgresql://postgres:postgres@localhost/restfulpy_boilerplate_dev
  test_url: postgresql://postgres:postgres@localhost/restfulpy_boilerplate_test
  administrative_url: postgresql://postgres:postgres@localhost/postgres
```

#### Remove old abd create a new database **TAKE CARE ABOUT USING THAT**

    $ restfulpy-boilerplate admin create-db --drop --basedata [or instead of --basedata, --mockup]

#### Drop old database: **TAKE CARE ABOUT USING THAT**

    $ restfulpy-boilerplate [-c path/to/config.yml] admin drop-db

#### Create database

    $ restfulpy-boilerplate [-c path/to/config.yml] admin create-db

Or, you can add `--drop` to drop the previously created database: **TAKE CARE ABOUT USING THAT**

    $ restfulpy-boilerplate [-c path/to/config.yml] admin create-db --drop
    
#### Create database object

    $ restfulpy-boilerplate [-c path/to/config.yml] admin setup-db

#### Database migration

    $ restfulpy-boilerplate migrate upgrade head

#### Insert Base data

    $ restfulpy-boilerplate [-c path/to/config.yml] admin base-data
    
#### Insert Mockup data

    $ restfulpy-boilerplate [-c path/to/config.yml] dev mockup-data
    
### Unittests

    $ nosetests
    
### Serving

- Using python builtin http server

```bash
$ restfulpy-boilerplate [-c path/to/config.yml] serve
```    

- Gunicorn

```bash
$ ./gunicorn
```
