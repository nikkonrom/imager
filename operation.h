#ifndef OPERATION_H
#define OPERATION_H
#include <QImage>

class Operation
{
public:
    explicit Operation(QImage);
private:
    QImage inputImage;
    virtual QImage execute(QImage);
};

#endif // OPERATION_H
