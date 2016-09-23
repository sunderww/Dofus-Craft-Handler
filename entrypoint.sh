#! /bin/bash

shift $((OPTIND-1)) # Reset in case getopts has been used previously in the shell.

# Initialize variables and parse arguments
action=bash
verbose=""
debug=""
port=5005

if [[ $# -gt 0 ]]; then
  action=$1
  OPTIND=2;
fi

while getopts ":dDvp:" opt; do
  case $opt in
    d) debug="-d" ;;
    D) debug="" ;;
    v) verbose="-v" ;;
    p) port=$OPTARG ;;

    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done


case $action in
  bash) exec /bin/bash ;;
  test) exec python -m unittest discover -b ;;

  start)
    exec python app.py $debug $verbose runserver -h 0.0.0.0 -p $port
    ;;

  *)
    echo "Invalid command $action"
    exit 1
    ;;
esac
