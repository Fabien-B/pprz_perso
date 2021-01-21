# pprz_perso

Synchronise all files that should not be tracked or changed in the main repo to this directory. You can then make a git repo of this directory and track them from this repo.

## Sync

Use `sync.sh` to synchronise your custom conf with the Paparazzi repo.

Untracked files will be copied to your custom conf, as well as all files that exists in your custom conf and in Paparazzi, whether it is tracked or not. 
This means that if you want to save in your custom conf a file tracked by git, you first have to copy it in your custom conf.

Files that do not exists in the Paparazzi repo will be deleted from your custom conf.

## Restore

`restore.sh` copy all files from your custom conf to the Paparazzi repo.
