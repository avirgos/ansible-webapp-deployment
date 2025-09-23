<!-- DOCSIBLE START -->

# 📃 Role overview

## flask_web



Description: Deploy Flask web server

| Field                | Value           |
|--------------------- |-----------------|
| `README.md` update        | 22/09/2025 |












### Tasks


#### File: `tasks/main.yml`

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| Install Flask package | `ansible.builtin.pip` | False |
| Copy app.py file | `ansible.builtin.copy` | False |
| Copy environment file | `ansible.builtin.copy` | False |
| Stop Flask server if running | `ansible.builtin.command` | False |
| Start Flask server with environment variables | `ansible.builtin.shell` | False |


## Task Flow Graph



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

  Start-->|Task| Install_Flask_package0[install flask package]:::task
  Install_Flask_package0-->|Task| Copy_app_py_file1[copy app py file]:::task
  Copy_app_py_file1-->|Task| Copy_environment_file2[copy environment file]:::task
  Copy_environment_file2-->|Task| Stop_Flask_server_if_running3[stop flask server if running]:::task
  Stop_Flask_server_if_running3-->|Task| Start_Flask_server_with_environment_variables4[start flask server with environment variables]:::task
  Start_Flask_server_with_environment_variables4-->End
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
