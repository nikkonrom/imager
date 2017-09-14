#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    bool loadFile(const QString &);
    ~MainWindow();

private slots:
    void on_actionOpen_triggered();

    void on_pushButton_clicked();

private:
    Ui::MainWindow *ui;
    void createActions();
    void setImage(const QImage &newImage);

    QImage inputImage;

};

#endif // MAINWINDOW_H
