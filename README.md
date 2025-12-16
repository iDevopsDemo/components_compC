# DataVisualizer (comp-c)

This component read messages from different storages like mysql or log file and visualize those in a simple web-based diagram.

## How to use

Just start the docker container with:

```sh
docker run --rm --name datavisualizer docker.artifactory.mydevops.info/xo-sample/comp-c
```

### Optional Parameters

The following environment variables are available to adjust the behavior:

* **DATACOLLECTOR_STORAGE** the storage class to use. Currently available: dummy, mysql(default)

Based on the selected storage class additional parameters are available:

* MYSQL
  * **STORAGE_MYSQL_HOST** ip address of the mysql db (default: 172.17.0.1)
  * **STORAGE_MYSQL_PORT** port of the mysql db (default: 3306)
  * **STORAGE_MYSQL_DB** database to use (default: xo)
  * **STORAGE_MYSQL_USER** username (default: admin)
  * **STORAGE_MYSQL_PASS** password (default: mysecret)

```sh
docker run --rm --name datavisualizer -e DATACOLLECTOR_STORAGE=mysql docker.artifactory.mydevops.info/xo-sample/comp-c
```

## TODOs

* For now we have no tests at all.
* We need to add proper testing stages into the gitlab-ci
* Only some testing
