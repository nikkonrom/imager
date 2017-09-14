#include "operation.h"

Operation::Operation(QImage inputImage)
{
    this->inputImage = inputImage;
}

 QImage Operation::execute(QImage source){
    return source;
}
