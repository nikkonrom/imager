#ifndef OPERATION_H
#define OPERATION_H
#include <QImage>

class Operation
{
public:
    void setImage(QImage image);
    virtual QImage execute();
private:
    QImage inputImage;

};

#endif // OPERATION_H
