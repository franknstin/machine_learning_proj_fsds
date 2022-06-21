# machine_learning_proj_fsds
First ML proect of the FSDS batch


Software and account Requirement.

1. Github Account
2. Heroku Account
3. VS Code IDE
4. GIT cli
5. GIT Documentation

creating conda environment
,,,
conda create -p venv python==3.7 -y
,,,,

,,,,,
,,,,,
pip install -r requirements.txt
,,,,,
,,,,,


Git documentation[https://git-scm.com/docs/git]


information needed from heroku to set the CI CD pipeline

1. heroku email = anmhatre94@gmail.com
2. heroku api key = <>
3. heroku app name = regression-app-ml

Build docker image
''''
docker build -t <image_name>:<tagname> .

 Note: image name for docker must be lowercase



 to list docker images

 '''
 docker images
 ,,,,


 Run docker image

 ,,,
 docker run -p 5000:5000 -e PORT=5000 9b0af0734997
,,,,


to check running containers in docker
,,,
docker ps
,,,,


to stop docker container
,,,
docker stop <container_id>

 