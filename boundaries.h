#ifndef BOUNDARIES_H
#define BOUNDARIES_H
#include <operation.h>

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

using namespace cv;

class Boundaries : public Operation
{
public:
    Boundaries();
    QImage execute(int value);

private:
    inline QImage  cvMatToQImage( const cv::Mat & );
    inline Mat QImageToCvMat(const QImage &inImage, bool inCloneImageData);
    Mat cannyThreshold ();

    Mat inputMat, inputMatGrayScaled;
    Mat outputMap, detectedEdges;

    int edgeThresh = 1;
    int ratio = 2;
    int kernelSize = 3;
};



#endif // BOUNDARIES_H
