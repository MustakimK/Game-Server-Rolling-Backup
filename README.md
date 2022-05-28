# Game-Server-Rolling-Backup

Creates backups at fixed intervals.

## Testing
1. [Install Poetry](https://python-poetry.org/docs/#installation) 
1. `poetry install` 
2. `poetry run pytest`

## Building Docker
`docker build . -t mustakim/game-backup:latest`

## Environment Variables
`SAVE_DIR` Directory saves are read from
`BACKUP_DIR` Directory where backups go
`BACKUP_FREQUENCY` How often backups are made. Example: `1h`
`OLDEST_BACKUP_AGE` How often backups are kept. Example: `1w`

## Example docker-compose
```yaml
version: "2.1"
services: 
  backups:
    image: backup:latest
    environment:
      SAVE_DIR: /saves
      BACKUP_DIR: /backups
      BACKUP_FREQUENCY: 1h
      OLDEST_BACKUP_AGE: 1w
    volumes:
      - ./saves:/saves:ro
      - ./backups:/backups  
```