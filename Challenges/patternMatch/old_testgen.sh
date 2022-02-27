#On windows, you can use the linux subsystem, then run testgen.sh
# source "./assert.sh"
#first use dos2unix testgen.sh to get rid of windows characters
assert ()                 #  If condition false,
{                         #+ exit from script
                          #+ with appropriate error message.
  E_PARAM_ERR=98
  E_ASSERT_FAILED=99


  if [ -z "$2" ]          #  Not enough parameters passed
  then                    #+ to assert() function.
    return $E_PARAM_ERR   #  No damage done.
  fi

  lineno=$2

  if [ ! $1 ] 
  then
    echo "Assertion failed:  \"$1\""
    echo "File \"$0\", line $lineno"    # Give name of file and line number.
    exit $E_ASSERT_FAILED
  # else
  #   return
  #   and continue executing the script.
  fi  
} # Insert a similar assert() function into a script you need to debug. 
#remove existing input and output
[[ -e input/ ]] && rm -r input/ 
[[ -e output/ ]] && rm -r output/ 
mkdir -p input
mkdir -p output

#copy over samples
[[ -e samples/input ]] && cp -r samples/input ./
[[ -e samples/output ]] && cp -r samples/output ./

 
for i in {2..50}
do
  echo $i | python3 ./mkin.py > input/input$i.txt
  a=python3 ./solutions/sol.py < input/input$i.txt
  b=python3 ./solutions/sol.py < input/input$i.txt
  echo $a  
  condition="$a == $b"
  assert "$condition"
  echo $i
done

rm -rf cases.zip
zip -r cases input output
