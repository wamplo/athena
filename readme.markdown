      ___,      _                       
     /   |     | |                      
    |    | _|_ | |     _   _  _    __,  
    |    |  |  |/ \   |/  / |/ |  /  |  
     \__/\_/|_/|   |_/|__/  |  |_/\_/|_/ optimzing with :heart:

Athena is the goddess of wisdom, courage, inspiration, civilization, law and justice, just warfare, mathematics, strength, strategy, the arts, crafts, and skill. 

## What she does

she compiles a folder `/views` into optimized views `/views_cdn` becouse bandwith and peformance matters

## Folders

    /_old
    old stuff
    /anthena
        - /bin
        where executable is on
            - /_old 
            old stuff
            - /jpeg8dexe
            http://sylvana.net/jpeg-bin/
            - /muncher
            https://github.com/ccampbell/html-muncher
            - googlecc.jar
            code.google.com/closure/
            - optipng-0.6.5.exe
            http://optipng.sourceforge.net/
        - /lib
            - /core 
            core library
            - /vendors_1
            example, if use vendors
            - /vendors_2
            example, if use vendors
        python scripts
        - /_old old stuff
        - /wiki docs
    /build.py

## How

- Instal python via Cygwin http://cygwin.com/install.html (recommanded) or Python via http://www.python.org/download/
- Via command promt Cygwin with Python + Java run `./build.py` in /engine/scripts/anthena
- *Magic happens here*
- Check in views_cdn/folder/index.html for the result(check index.html same in views)

## Todo

- Refactoring(clean and tidy)
- Optimize(y n optimize?)
- HACK!(add some more feature)
    - http://code.google.com/p/closure-stylesheets/ add this
    - http://code.google.com/closure/templates/ add this
    - Deprecate https://github.com/ccampbell/html-muncher

## Tips

add in .git/config

    [alias]
        addremove = !git add . && git ls-files --deleted | xargs --no-run-if-empty git rm

it will be

    git addremove (replace git add and remove)
    git commit -m "something"
    git push

and

    git config --global core.excludesfile ~/.gitignore

so the compiled files in views_cdn will not be included

## Licence

Everything you write is on a *proprietary software licence* for vendors and others we inherit their licence. but maybe this one will be opensourced.