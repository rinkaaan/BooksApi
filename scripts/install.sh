WORKPLACE="$HOME/workplace"
WORKSPACE="$WORKPLACE/Books"

(
  cd "$WORKSPACE/PythonUtils"
  pip install .
  rm -rf build
)
