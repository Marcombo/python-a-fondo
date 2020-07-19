import ftplib

if __name__ == '__main__':
    ftp = ftplib.FTP('mirrors.up.pt')
    ftp.login()
    print(ftp.getwelcome())
    print(ftp.dir())
    print(ftp.cwd('pub/ubuntu-releases/focal'))
    print(ftp.nlst())
    print(ftp.size('ubuntu-20.04-desktop-amd64.iso'))
    with open('ftp_ubuntu_focal_MD5SUMS', 'wb') as fp:
        ftp.retrbinary('RETR MD5SUMS', fp.write)

    ftp.quit()
