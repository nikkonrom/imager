#include "operation.h"

void Operation::setImage(QImage inputImage)
{
    this->inputImage = inputImage;
}

QImage Operation::execute(){
    return this->inputImage;
}


