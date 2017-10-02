#include <QtGui/QPainter>
#include "scaledpixmap.h"

ScaledPixmap::ScaledPixmap(QWidget* parent)
    : QLabel(parent)
    , m_overscalingEnabled(true)
    , m_keepAspectRatio(true)
{}

ScaledPixmap::~ScaledPixmap()
{}

QPixmap ScaledPixmap::pixmap() const
{
    return m_pixmap;
}

void ScaledPixmap::setScaledPixmap(const QPixmap& pixmap)
{
    m_pixmap = pixmap;
    m_originalSize = pixmap.size();
    update();
}

void ScaledPixmap::setOverscaleEnabled(bool enable)
{
    m_overscalingEnabled = enable;
    update();
}

void ScaledPixmap::setKeepAspectRatioEnabled(bool enable)
{
    m_keepAspectRatio = enable;
    update();
}

bool ScaledPixmap::overscaleEnabled() const
{
    return m_overscalingEnabled;
}

bool ScaledPixmap::keepAspectRatioEnabled() const
{
    return m_keepAspectRatio;
}

void ScaledPixmap::loadPixmapData(QPixmap outputMap) {
    if (!outputMap.isNull())
        setScaledPixmap(outputMap);
}

void ScaledPixmap::loadPixmapData(const QString& path)
{
    QPixmap pixmap(path);

    if (!pixmap.isNull())
        setScaledPixmap(pixmap);
}

bool ScaledPixmap::fitsToScreen(const QSize& screenSize)
{
    return (screenSize.width() >= m_originalSize.width()) && (screenSize.height() >= m_originalSize.height());
}

void ScaledPixmap::paintEvent(QPaintEvent* event)
{
    QPainter painter(this);

    if (!m_pixmap.isNull())
    {
        QPoint centerPoint(0, 0);
        QSize scaledSize = overscaleEnabled() ? size() : (fitsToScreen(size()) ? m_originalSize : size());

        QPixmap scaledPixmap = m_pixmap.scaled(scaledSize, m_keepAspectRatio ? Qt::KeepAspectRatio : Qt::IgnoreAspectRatio);

        centerPoint.setX((size().width() - scaledPixmap.width()) / 2);
        centerPoint.setY((size().height() - scaledPixmap.height()) / 2);

        painter.drawPixmap(centerPoint, scaledPixmap);
    }

    QLabel::paintEvent(event);
}
