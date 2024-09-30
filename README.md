This is a [Django](https://www.djangoproject.com/) project deployed to AWS using [Terraform](https://www.terraform.io/).
## Getting Started

- Clone the repo into your project directory
```
	git clone git@github.com:codinci/assessment_task.git
```

- Once loaded up convert the .env.example in the django-aws-backend and django-aws-infrastructure directories with the   associated values

- In windows navigate to the django-aws-backend directory and on the bash terminal run:
```
source venv/Scripts/activate

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

```
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) with your browser to see the result.


This should run the project on the local server 127.0.0.1:8000

- To run docker

```
 docker-compose up -d --build
```
Open [http://localhost:8000](http://localhost:8000) with your browser to see the result.

- For the infrastructure navigate to the django-aws-infrastructure and run:
```
terraform init
terraform apply

docker build . -t <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/django-aws-backend:latest
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com
docker push <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/django-aws-backend:latest

```

## Learn More

The following articles and documentation were used in the building of this application:
- [Infrastructure and deployment](https://dev.to/daiquiri_team/deploying-django-application-on-aws-with-terraform-minimal-working-setup-587g)
- [OpenID Connect](https://learndjango.com/tutorials/django-allauth-tutorial)
- [Django Allauth Documentation](https://django-allauth.readthedocs.io/en/latest/installation/quickstart.html)
- [Africa's Talking Documentation](https://developers.africastalking.com/tutorials/messaging-101-sending-an-sms/l/5faae82ad544889a10240d27)
- [Africa's Talking Tutorial](https://sayari3.com/articles/17-how-to-send-sms-using-django-and-africastalking-api/)

