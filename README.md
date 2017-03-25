# tyler dashboard

I have a home file server/media player/compute node used by the whole family. Sometimes I'm not available to perform maintenance tasks on it. This is a small dashboard to allow normal people to do maintenance tasks.

* Restart Kodi

## TODO

* Is the Internet working?
* Are there any alerts (e.g. disk failures)

## Deployment

Deployment is manual right now.

* `git clone` on the server
* Create a virtualenv and `pip install -r deploy/requirements.txt`
* Copy `deploy/dash.conf` to `/etc/init/` (it's Ubuntu 14.04)
* `service restart dash`
