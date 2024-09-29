variable "region" {
  description = "The AWS region to create resources in."
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name to use in resource names"
  default     = "django-aws"
}

variable "availability_zones" {
  description = "Availability zones"
  default     = ["us-east-1a", "us-east-1c"]
}

variable "ecs_prod_backend_retention_days" {
  description = "Retention period for backend logs"
  default     = 30
}

variable "prod_rds_db_name" {
  description = "RDS database name"
  default     = "customer_orders_db"
}
variable "prod_rds_username" {
  description = "RDS database username"
  default     = "rds_user"
}
variable "prod_rds_password" {
  description = "postgres password for production DB"
}
variable "prod_rds_instance_class" {
  description = "RDS instance type"
  default     = "db.t4g.micro"
}