#ifndef BOUNDARIES_H
#define BOUNDARIES_H
#include <operation.h>

#include <opencv2/core/core.hpp>

class Boundaries : public Operation
{
public:
    Boundaries();
    QImage execute();
private:
    QImage mat_to_qimage_ref(cv::Mat &mat, QImage::Format format);
    cv::Mat qimage_to_mat_ref(QImage &img, int format);
};

#endif // BOUNDARIES_H
