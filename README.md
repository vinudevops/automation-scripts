# automation-scripts
Centralized repository for DevOps automation scripts and configurations

├── main.tf
├── variables.tf
├── outputs.tf
├── terraform.tfvars
├── providers.tf
├── modules
│   ├── module1
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   ├── ...
│   ├── module2
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   ├── ...
│   └── ...
├── environments
│   ├── dev
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   ├── terraform.tfvars
│   │   ├── providers.tf
│   │   └── ...
│   ├── stage
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   ├── terraform.tfvars
│   │   ├── providers.tf
│   │   └── ...
│   ├── prod
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   ├── terraform.tfvars
│   │   ├── providers.tf
│   │   └── ...
│   └── ...
└── .terraform
    ├── terraform.tfstate
    ├── terraform.tfstate.backup
    └── ...
