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

    void on_loadButton_clicked();

    void on_boudaries_button_clicked();

private:
    Ui::MainWindow *ui;
    void createActions();
    void setImage(const QImage &newImage);

    QImage inputImage;
    QImage outputImage;

};

#endif // MAINWINDOW_H
