## Publishing the package
[using python-poetry to publish to test.pypi.org - Stack Overflow](https://stackoverflow.com/questions/68882603/using-python-poetry-to-publish-to-test-pypi-org)

> ## One time setup ( per host / environment)
> 
> ### PYPI test
> 
> -   add repository to poetry config `poetry config repositories.test-pypi https://test.pypi.org/legacy/`
>     
> -   get token from [https://test.pypi.org/manage/account/token/](https://test.pypi.org/manage/account/token/)
>     
> -   store token using `poetry config pypi-token.test-pypi pypi-YYYYYYYY`
>     
> 
> _Note:_ 'test-pypi' is the name of the repository
> 
> ### PYPI Production
> 
> -   get token from [https://pypi.org/manage/account/token/](https://pypi.org/manage/account/token/)
> -   store token using `poetry config pypi-token.pypi pypi-XXXXXXXX`
> 
> ## Bump version
> 
> -   `poetry version prerelease`
> -   `poetry version patch`
> 
> ## Poetry Publish
> 
> To test
> 
> -   `poetry publish --build -r test-pypi`
> 
> To PyPi
> 
> -   `poetry publish --build`