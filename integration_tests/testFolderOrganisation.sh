#!/bin/bash

pushd ..
rm -rf .secrets

pushd src
python Trako.py 
if [[ $? -eq 1 ]]
then
    echo "Pass check does dir exist (it does not exist)"
    popd
    if [[ -d .secrets ]]
    then
        echo "Pass dir created"
        if [[ -f .secrets/token ]]
        then
            echo "Pass file created"
        else
            echo "Fail file created"
        fi
    else 
        echo "Fail dir created"
    fi
else
    echo "Fail check does dir exist (it does not exist)"
fi
popd