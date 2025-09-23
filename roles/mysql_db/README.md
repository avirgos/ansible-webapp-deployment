<!-- DOCSIBLE START -->

# 📃 Role overview

## mysql_db



Description: Deploy a MySQL database

| Field                | Value           |
|--------------------- |-----------------|
| `README.md` update        | 22/09/2025 |








### Defaults

**These are static variables with LOWER priority**

#### File: `defaults/main.yml`

| Var          | Type         | Value       |
|--------------|--------------|-------------|
| [`mysql_db_db_name`](defaults/main.yml#L2)   | str | `employee_db` |    
| [`mysql_db_db_user`](defaults/main.yml#L3)   | str | `db_user` |    

### Vars

**These are variables with HIGHER priority**
#### File: `vars/vault.yml`

| Var          | Type         | Value       |
|--------------|--------------|-------------|
| [`mysql_db_root_password`](vars/vault.yml#L2)   | str | `ENCRYPTED_WITH_ANSIBLE_VAULT` |    

### Tasks


#### File: `tasks/load-secrets.yml`

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| Load MySQL secrets | `ansible.builtin.include_vars` | False |

#### File: `tasks/main.yml`

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| Load MySQL secrets | `ansible.builtin.include_tasks` | False |
| Install MySQL database | `ansible.builtin.apt` | False |
| Start MySQL service | `ansible.builtin.command` | False |
| Create `.my.cnf` file | `ansible.builtin.copy` | False |
| Install MySQL python module | `ansible.builtin.pip` | False |
| Create app database | `community.mysql.mysql_db` | False |
| Create database user | `community.mysql.mysql_user` | False |
| Create `employees` table | `community.mysql.mysql_query` | False |
| Insert sample data into `employees` table | `community.mysql.mysql_query` | False |


## Task Flow Graph



### Graph for `load-secrets.yml`

```mermaid
flowchart TD
Start
classDef block stroke:#3498db,stroke-width:2px;
classDef task stroke:#4b76bb,stroke-width:2px;
classDef includeTasks stroke:#16a085,stroke-width:2px;
classDef importTasks stroke:#34495e,stroke-width:2px;
classDef includeRole stroke:#2980b9,stroke-width:2px;
classDef importRole stroke:#699ba7,stroke-width:2px;
classDef includeVars stroke:#8e44ad,stroke-width:2px;
classDef rescue stroke:#665352,stroke-width:2px;

  Start-->|Include vars| Load_MySQL_secrets____role_path____vars_vault_yml_0[load mysql secrets<br>include_vars:    role path    vars vault yml]:::includeVars
  Load_MySQL_secrets____role_path____vars_vault_yml_0-->End
```


### Graph for `main.yml`

```mermaid
flowchart TD
Start
classDef block stroke:#3498db,stroke-width:2px;
classDef task stroke:#4b76bb,stroke-width:2px;
classDef includeTasks stroke:#16a085,stroke-width:2px;
classDef importTasks stroke:#34495e,stroke-width:2px;
classDef includeRole stroke:#2980b9,stroke-width:2px;
classDef importRole stroke:#699ba7,stroke-width:2px;
classDef includeVars stroke:#8e44ad,stroke-width:2px;
classDef rescue stroke:#665352,stroke-width:2px;

  Start-->|Include task| Load_MySQL_secrets_load_secrets_yml_0[load mysql secrets<br>include_task: load secrets yml]:::includeTasks
  Load_MySQL_secrets_load_secrets_yml_0-->|Task| Install_MySQL_database1[install mysql database]:::task
  Install_MySQL_database1-->|Task| Start_MySQL_service2[start mysql service]:::task
  Start_MySQL_service2-->|Task| Create___my_cnf__file3[create   my cnf  file]:::task
  Create___my_cnf__file3-->|Task| Install_MySQL_python_module4[install mysql python module]:::task
  Install_MySQL_python_module4-->|Task| Create_app_database5[create app database]:::task
  Create_app_database5-->|Task| Create_database_user6[create database user]:::task
  Create_database_user6-->|Task| Create__employees__table7[create  employees  table]:::task
  Create__employees__table7-->|Task| Insert_sample_data_into__employees__table8[insert sample data into  employees  table]:::task
  Insert_sample_data_into__employees__table8-->End
```


## Author Information

Antoine Virgos (@avirgos)

#### License

MIT

#### Minimum Ansible Version

2.1

#### Platforms

No platforms specified.

#### Dependencies

No dependencies specified.
<!-- DOCSIBLE END -->
