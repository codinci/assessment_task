[
  {
    "name": "${name}",
    "image": "${image}",
    "essential": true,
    "links": [],
    "portMappings": [
      {
        "containerPort": 8000,
        "hostPort": 8000,
        "protocol": "tcp"
      }
    ],
	"environment": [
      {
        "name": "DATABASE_URL",
        "value": "postgresql://${rds_username}:${rds_password}@${rds_hostname}:5432/${rds_db_name}"
      },
      {
        "name": "HUB_CLIENT_ID",
        "value": "{hub_client_id}"
      },
       {
        "name": "HUB_SECRET_KEY",
        "value": "{hub_secret_key}"
      },
       {
        "name": "AFRICAS_TALKING_USERNAME",
        "value": "{africas_talking_username}"
      },
       {
        "name": "AFRICAS_TALKING_API_KEY",
        "value": "{africas_talking_api_key}"
      },

    ],
    "command": ${jsonencode(command)},
    "logConfiguration": {
      "logDriver": "awslogs",
      "options": {
        "awslogs-group": "${log_group}",
        "awslogs-region": "${region}",
        "awslogs-stream-prefix": "${log_stream}"
      }
    }
  }
]