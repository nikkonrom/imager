#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "boundaries.h"

#include <QFileDialog>
#include <QStandardPaths>
#include <QImageReader>
#include <QImageWriter>
#include <QMessageBox>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    this->setWindowTitle("Imager");
    connect(ui->keepAspectRatioCheckBox, &QCheckBox::stateChanged, [&](int state)
    {
        ui->inputLabel->setKeepAspectRatioEnabled(state == Qt::Checked);
        ui->outputLabel->setKeepAspectRatioEnabled(state == Qt::Checked);
    });

    connect(ui->overscaleCheckBox, &QCheckBox::stateChanged, [&](int state)
    {
        ui->inputLabel->setOverscaleEnabled(state == Qt::Checked);
        ui->outputLabel->setOverscaleEnabled(state == Qt::Checked);
    });

    connect(ui->loadButton, &QPushButton::clicked, [&]()
    {
        ui->inputLabel->loadPixmapData(QFileDialog::getOpenFileName(this));
    });

    createActions();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::createActions(){

}

void MainWindow::setImage(const QImage &newImage)
{
    inputImage = newImage;
    ui->inputLabel->setPixmap(QPixmap::fromImage(inputImage));
    //scaleFactor = 1.0;

    /*scrollArea->setVisible(true);
    printAct->setEnabled(true);
    fitToWindowAct->setEnabled(true);
    updateActions()

    if (!fitToWindowAct->isChecked())
        imageLabel->adjustSize();*/
}

bool MainWindow::loadFile(const QString &fileName)
{
    QImageReader reader(fileName);
    reader.setAutoTransform(true);
    const QImage newImage = reader.read();
    if (newImage.isNull()) {
        QMessageBox::information(this, QGuiApplication::applicationDisplayName(),
                                 tr("Cannot load %1: %2")
                                 .arg(QDir::toNativeSeparators(fileName), reader.errorString()));
        return false;
    }

    setImage(newImage);

    setWindowFilePath(fileName);

    const QString message = tr("Opened \"%1\", %2x%3, Depth: %4")
        .arg(QDir::toNativeSeparators(fileName)).arg(inputImage.width()).arg(inputImage.height()).arg(inputImage.depth());
    statusBar()->showMessage(message);
    return true;
}

static void initializeImageFileDialog(QFileDialog &dialog, QFileDialog::AcceptMode acceptMode)
{
    static bool firstDialog = true;

    if (firstDialog) {
        firstDialog = false;
        const QStringList picturesLocations = QStandardPaths::standardLocations(QStandardPaths::PicturesLocation);
        dialog.setDirectory(picturesLocations.isEmpty() ? QDir::currentPath() : picturesLocations.last());
    }

    QStringList mimeTypeFilters;
    const QByteArrayList supportedMimeTypes = acceptMode == QFileDialog::AcceptOpen
        ? QImageReader::supportedMimeTypes() : QImageWriter::supportedMimeTypes();
    foreach (const QByteArray &mimeTypeName, supportedMimeTypes)
        mimeTypeFilters.append(mimeTypeName);
    mimeTypeFilters.sort();
    dialog.setMimeTypeFilters(mimeTypeFilters);
    dialog.selectMimeTypeFilter("image/jpeg");
    if (acceptMode == QFileDialog::AcceptSave)
        dialog.setDefaultSuffix("jpg");
}
/*
void MainWindow::on_actionOpen_triggered()
{
    QFileDialog dialog(this, tr("Open File"));
    initializeImageFileDialog(dialog, QFileDialog::AcceptOpen);

    while (dialog.exec() == QDialog::Accepted && !loadFile(dialog.selectedFiles().first())) {}
}

void MainWindow::on_loadButton_clicked()
{
    MainWindow::on_actionOpen_triggered();
}
*/

void MainWindow::on_boudaries_button_clicked()
{

    Boundaries boundaries_operation;
    boundaries_operation.setImage(ui->inputLabel->pixmap().toImage());
    outputImage = boundaries_operation.execute(ui->horizontalSlider->value());
    ui->outputLabel->loadPixmapData(QPixmap::fromImage(outputImage));
}
