# Ghost base

A Dockerized environment ready for developing and deploying Ghost applications.

![Ghost + Docker logo](docs/ghost-docker.png "Ghost + Docker logo")

## Configuration

Start by copying the example config provided in the `./config/.dist` folder to `./config/`. Four files are provided:

```
config/.dist
├── config.development.json
├── config.production.json
├── development.env
└── production.env
```

You'll need to edit `config/development.env` and `config/production.env` and fill the missing values.

```
ghost-base $ cp config/.dist/* config/

ghost-base $ vim config/development.env
MYSQL_DATABASE=ghost_dev
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_ROOT_PASSWORD=
NODE_ENV=development
NPM_CONFIG_LOGLEVEL=debug

ghost-base $ vim config/production.env
MYSQL_DATABASE=ghost_prod
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_ROOT_PASSWORD=
NODE_ENV=production
NPM_CONFIG_LOGLEVEL=info
```

> Note: This repo contains a `.gitignore` rule that will make sure that your `config/*.env` and `config/*.json` are not commited to Git as they contain sensitive information (database credentials).

## Ghost Database(s)

For both the development and production environments described below [Docker Volumes](https://docs.docker.com/engine/admin/volumes/volumes/) are used to persist the Ghost database.

Please be aware that stopping your blog with `docker-compose down -v` or by running a cleanup task such as `docker system prune` when your blog is stopped will result in the Docker Volumes above being *removed*. Make sure you backup!

## Development environment

To start your Ghost blog in development mode, using [_nodemon_](https://nodemon.io/) in order to pick up changes automatically, run:

```
ghost-base $ docker-compose up ghost -d
```

This development environment is especially useful if you are [making changes to a theme](https://docs.ghost.org/docs/install-local#section-developing-themes).

Your Ghost blog will now be running on [http://localhost:12368/](http://localhost:12368/). Happy hacking.

To stop it do:
```
ghost-base $ docker-compose stop ghost
```

## Production environment

Once you're happy with the changes to your theme it's now time to boot your app in production mode. Start by building the Docker image containing your blog files.

```
ghost-base $ docker-compose build ghost
```

Now start Ghost in production mode and use Nginx (`web`) as reverse proxy:
```
ghost-base $ docker-compose -f docker-compose.yml -f docker-compose.prod.yml up ghost -d
```

Your Ghost blog will now be running on [http://localhost:2367/](http://localhost:2367/). Enjoy.

To stop it do:
```
ghost-base $ docker-compose -f docker-compose.yml -f docker-compose.prod.yml stop web
```

## Bonus: Generate static content using Buster

By using [Buster](https://github.com/axitkhurana/buster) we can generate static content from a running Ghost instance and serve these files directly using something like [GitHub Pages](https://pages.github.com/).

To generate static files and store them in `build/buster` do:

```
ghost-base $ docker-compose -f docker-compose.yml -f docker-compose.prod.yml run --rm buster generate
```

To preview your static website locally before pushing to GitHub Pages start the `live` service:


```
ghost-base $ docker-compose up live
```

and browse the website at [http://localhost:80](http://localhost:80).

## Development vs Production databases

As you can see in our `docker-compose*.yml` files we are using two data volumes, separating development and production databases. This allows you to make changes while testing the blog without affecting production data.

 However, if you prefer, you can combine `*dev` and `*prod` services and data volumes into a single `db` service and data volume sharing the same data for development and production. Make sure you also adjust the database name in the `config/*.env` files.
 
## License

This project is licensed under the [MIT License](LICENSE).