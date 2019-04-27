#!/usr/bin/env bash

# Check if svm is trained
if [ -f ./trained.obj ]; then
    echo "Trained SVM exists"
elif [ -f ../train_svm/trained.obj ]; then
    echo "Trained SVM exists"
    cp ../train_svm/trained.obj .
else
    ./../train_svm/main.py ../train_svm/data
fi

# Start C Program to gather data
if [ -f astrapull ]; then
    echo "C program exists"
else
    cd ../../samples/
    cmake . && make
    cd ../python/live_classification && cp ../../samples/bin/BodyReaderPollStdOut astrapull
fi

./astrapull | python3 live_classifier.py