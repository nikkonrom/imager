#pragma once

#include <QtWidgets/QLabel>
#include <QtGui/QPixmap>

QT_FORWARD_DECLARE_CLASS(QPaintEvent)

class ScaledPixmap : public QLabel
{
    Q_OBJECT

public:
    explicit ScaledPixmap(QWidget* parent = nullptr);
    virtual ~ScaledPixmap();

public:
    QPixmap pixmap() const;

    bool overscaleEnabled() const;
    bool keepAspectRatioEnabled() const;

public slots:
    void setScaledPixmap(const QPixmap& pixmap);
    void loadPixmapData(const QString& path);
    void loadPixmapData(QPixmap outputMap);

    void setOverscaleEnabled(bool enable = true);
    void setKeepAspectRatioEnabled(bool enable = true);

signals:
    void loadFinished(bool);

protected:
    void paintEvent(QPaintEvent*);

private:
    bool fitsToScreen(const QSize& screenSize);

private:
    bool    m_keepAspectRatio;
    bool    m_overscalingEnabled;

    QPixmap m_pixmap;
    QSize   m_originalSize;
};
