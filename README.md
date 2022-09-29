# MachineLearingProjects
This is first my Machine Learing Projects

Software and Account Requirments,

1. [Github](https://github.com)
2. [Heroku](https://www.heroku.com/)
3. [VS code IDE](https://code.visualstudio.com/)
4. [git cli](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

creating virtual envirnment

```
python3 -m venev ./venv
```
Activating virtual envirnment

```
. venv/bin/activate
```
Install requirments file
pip install -r requirments.txt

1. HEROKU_EMAIL = syedsajjad62@gmail.com
2. HEROKU_API  = 6eae8a9d-b4a5-495a-936e-8a57753e40bb
3. HEROKU_APP_NAME = mlregression62

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```


> note: Image name for docker must be lowercase

To list docker images
```
docker images
```

TO Run Docker image
```
docker run -p 5000:5000 -e PORT=5000 50e0dff5595c
```

TO stop running continer
```
docker ps
```
To stop docker container
```
docker stop <container_id>
```