# ambition
(P.I. Joe Jarvis)


### Installation

    mkdir  ~/.venvs
    mkdir  ~/source
    
    # create VENV
    python3 -m venv ~/.venvs/ambition
    
    # activate VENV
    source ~/.venvs/ambition
    
    # update pip
    pip install -U pip ipython
    
    # clone main project
    cd ~/source/
    git https://github.com/botswana-harvard/ambition.git
    
    # install requirements
    cd ~/source/ambition
    pip install -r requirements.txt  # or production
    
    # create database
    mysql -u <user> -p -Bse 'create database ambition character set utf8;'
    
    # migrate
    python manage.py migrate
    
    # import required data
    python manage.py import_randomization_list
    python manage.py import_holidays
    
    # check for any obvious issues
    python manage.py check
    
    
    

 