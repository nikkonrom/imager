#include "boundaries.h"



Boundaries::Boundaries()
{

}

QImage mat_to_qimage_ref(cv::Mat &mat, QImage::Format format)
{
  return QImage(mat.data, mat.cols, mat.rows, mat.step, format);
}

cv::Mat qimage_to_mat_ref(QImage &img, int format)
{
    return cv::Mat(img.height(), img.width(),
            format, img.bits(), img.bytesPerLine());
}

QImage Boundaries::execute(){
    return this->inputImage;
}
