# youtube downloader
download youtube video, decrypt signature cipher, test on 2022.10.29 zh_TW.

```cmd
C:\Users\Username\Downloads>python youtube.py -u https://www.youtube.com/watch?v=piEyKyJ4pFg -h
Get User Argument
usage: youtube.py [-h] [-url URL] [-list] [-quality QUALITY] [-download] [-print PRINT]
                  [-fullPrint FULLPRINT] [-combine COMBINE] [-transform TRANSFORM]
                  [-remove REMOVE] [-audioOnly] [-videoOnly]

Youtube Video Downloader, Test on 2022.10.30 zh_TW.

optional arguments:
  -h, --help            show this help message and exit
  -url URL, -u URL      input a youtube url. (str)
  -list, -l             List all information of a youtube video, like video quality.
  -quality QUALITY, -q QUALITY
                        select a quality you want to view or download. Like Best, best, 1080,
                        720, 360, 240. (str, default:"")
  -download, -d         download the video. (required install ffmpeg on your device.)
  -print PRINT, -p PRINT
                        print the information and url that we get of a video. (int 1 or 0,
                        default:1)
  -fullPrint FULLPRINT, -fp FULLPRINT
                        print information and decrypt function that extract from base.js and
                        other debug values. (int 1 or 0, default:0)
  -combine COMBINE, -c COMBINE
                        after downloading, combine the video and audio or not. (int 1 or 0,
                        default:1)
  -transform TRANSFORM, -tr TRANSFORM
                        after downloading, transform the media format or not. (int 1 or 0,
                        default:1)
  -remove REMOVE, -r REMOVE
                        after downloading, remove the original medias we downloaded or not. (int
                        1 or 0, default:1)
  -audioOnly, -a        only download audio.
  -videoOnly, -v        only download video.
```
```cmd
Example:
python youtube.py -u https://www.youtube.com/watch?v=piEyKyJ4pFg
python youtube.py -u https://www.youtube.com/watch?v=piEyKyJ4pFg -list
python youtube.py -u https://www.youtube.com/watch?v=piEyKyJ4pFg -q best -download

Experiment:
python live.py -u "youtube video url which is live now" -list
python live.py -u "youtube video url which is live now" -q best -download
python combine.py -f "the folder that is created by live.py"
```
```cmd
C:\Users\Username\Downloads>python youtube.py -u https://www.youtube.com/watch?v=piEyKyJ4pFg -l
Get User Argument
Download Source Code From Youtube...
Type:      video/mp4; codecs="avc1.64002a", W×H  1920× 1080   1080P60, Fps  60, ContentLength 11491441.
Type:             video/webm; codecs="vp9", W×H  1920× 1080   1080P60, Fps  60, ContentLength 21524684.
Type:    video/mp4; codecs="av01.0.09M.08", W×H  1920× 1080   1080P60, Fps  60, ContentLength 20388193.
Type:      video/mp4; codecs="avc1.4d401f", W×H  1280×  720      720P, Fps  30, ContentLength 6739974.
Type:             video/webm; codecs="vp9", W×H  1280×  720      720P, Fps  30, ContentLength 8669807.
Type:      video/mp4; codecs="avc1.4d4020", W×H  1280×  720    720P60, Fps  60, ContentLength 4441714.
Type:             video/webm; codecs="vp9", W×H  1280×  720    720P60, Fps  60, ContentLength 8892222.
Type:    video/mp4; codecs="av01.0.08M.08", W×H  1280×  720    720P60, Fps  60, ContentLength 11289786.
Type:      video/mp4; codecs="avc1.4d401f", W×H   854×  480      480P, Fps  30, ContentLength 2481594.
Type:             video/webm; codecs="vp9", W×H   854×  480      480P, Fps  30, ContentLength 4589130.
Type:    video/mp4; codecs="av01.0.04M.08", W×H   854×  480      480P, Fps  30, ContentLength 4808813.
Type:      video/mp4; codecs="avc1.4d401e", W×H   640×  360      360P, Fps  30, ContentLength 1837997.
Type:             video/webm; codecs="vp9", W×H   640×  360      360P, Fps  30, ContentLength 3351050.
Type:    video/mp4; codecs="av01.0.01M.08", W×H   640×  360      360P, Fps  30, ContentLength 3175510.
Type:      video/mp4; codecs="avc1.4d4015", W×H   426×  240      240P, Fps  30, ContentLength 1131067.
Type:             video/webm; codecs="vp9", W×H   426×  240      240P, Fps  30, ContentLength 2204153.
Type:    video/mp4; codecs="av01.0.00M.08", W×H   426×  240      240P, Fps  30, ContentLength 2073347.
Type:      video/mp4; codecs="avc1.4d400c", W×H   256×  144      144P, Fps  30, ContentLength 707892.
Type:             video/webm; codecs="vp9", W×H   256×  144      144P, Fps  30, ContentLength 1780751.
Type:    video/mp4; codecs="av01.0.00M.08", W×H   256×  144      144P, Fps  30, ContentLength 1596870.
Type:        audio/mp4; codecs="mp4a.40.2", Bitrate  130494, Rate  44100, Channels 2, Quality  AUDIO_QUALITY_MEDIUM, ContentLength 3762144.
Type:            audio/webm; codecs="opus", Bitrate   60499, Rate  48000, Channels 2, Quality     AUDIO_QUALITY_LOW, ContentLength 1461482.
Type:            audio/webm; codecs="opus", Bitrate   79303, Rate  48000, Channels 2, Quality     AUDIO_QUALITY_LOW, ContentLength 1936759.
Type:            audio/webm; codecs="opus", Bitrate  150852, Rate  48000, Channels 2, Quality  AUDIO_QUALITY_MEDIUM, ContentLength 3822436.
```
```cmd
C:\Users\Username\Downloads>python youtube.py -u https://www.youtube.com/watch?v=piEyKyJ4pFg
Get User Argument
Download Source Code From Youtube...
Download Source Code From https://www.youtube.com/s/player/19fc75cf/player_ias.vflset/zh_TW/base.js


Type: video/mp4; codecs="avc1.64002a", W×H 1920×1080 1080P60, Fps 60, ContentLength 11491441.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=299&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=video%2Fmp4&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=11491441&dur=232.333&lmt=1653309795831239&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAJ3XDOBxRF9etotCVJEAv8zadd9970ctvqbLf9cot_guAiA6gBfVfYDa8V8dnRQKMVL5xt7nfIWB40v1ApBLjuYH0A%3D%3D&alr=yes&sig=AOq0QJ8wRQIgWudU77rfGjEV8GDAUiL87u1VD435PsswMVbgxghLNukCIQDAPD6BHc5_CUTOJWMk6KmNFbAkoFqVWKRShY_ILIisPQ%3D%3D


Type: video/webm; codecs="vp9", W×H 1920×1080 1080P60, Fps 60, ContentLength 21524684.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=303&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=video%2Fwebm&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=21524684&dur=232.333&lmt=1653318584845743&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgaFLotE1yK8wDVk5ANjYRiKUGL5nHglJNIvK_IffdPlECIQDOr_bSdZ8nC4aS71fEnFFsO2JciuOAil4jloQlfCv-8w%3D%3D&alr=yes&sig=AOq0QJ8wRQIgL31naqRyjSbJGX2--6tXGCFe79w0MEyMWlPqCvw2aEcCIQCKaCNZTnntiwBoUjI5z4suoBWuRM_g2lGz9XkbhoNnbw%3D%3D


Type: video/mp4; codecs="av01.0.09M.08", W×H 1920×1080 1080P60, Fps 60, ContentLength 20388193.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=399&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=video%2Fmp4&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=20388193&dur=232.333&lmt=1653309884687716&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4532434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhANMS9hEAAJlGG8WSivCkvOykU3obFLWVXZUNfTGaFdmuAiB54lFD-IkZNiN3x4PJtlDdlBCiPBlOIXDZs1Iq3Kml9Q%3D%3D&alr=yes&sig=AOq0QJ8wRgIhAMnUyCFnWPPyNkIB6Hm2IFuBiv0RLw9KJlQTcnzQ4ScrAiEAq5wrOzlildg63paPkmmIzG4OZbddYnV6Yvplrmnv3yw%3D


Type: video/mp4; codecs="avc1.4d401f", W×H 1280×720 720P, Fps 30, ContentLength 6739974.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=136&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=video%2Fmp4&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=6739974&dur=232.333&lmt=1653309686871534&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAOugm_8gzQ71zjBEXdb4V2awPprzIe24toIMxmnTj0_4AiBXleRjak33kii0F2lMoEvHFrQBAzC7HVs29UE-_QiOGA%3D%3D&alr=yes&sig=AOq0QJ8wRQIgc-kSNVqwloor3hQJ2VMKxVYijkueT73rSr3dJLohDJYCIQDIcH7Wwd_3i59hxpVUAG9LkSZkTuvWpcyRLRlOrQS3pw%3D%3D


Type: video/webm; codecs="vp9", W×H 1280×720 720P, Fps 30, ContentLength 8669807.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=247&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=video%2Fwebm&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=8669807&dur=232.333&lmt=1653318184388632&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgQnpKAUcH0-kU-6hFOExmvzmG58Il3ENbqFqXK4N2HjQCIQDYbxX1gobtRD1CEyEZ6kxF_iyXU8Gr5Qs2NlIFrCwlWA%3D%3D&alr=yes&sig=AOq0QJ8wRgIhAKjVzXOHpfxi-DN-O361zlQLXAXrFmNl5dSiCXtyaTHVAiEA6SqLKJ3TrT3nZMlz1sEllhf3f7l7P5xN7458MPSjt1k%3D


Type: video/mp4; codecs="avc1.4d4020", W×H 1280×720 720P60, Fps 60, ContentLength 4441714.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=298&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=video%2Fmp4&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=4441714&dur=232.333&lmt=1653309692326400&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJC-wORjasqUTvMbxPTRMUHz9yva4wC_5sc8x89yUytbAiEAkGXoNCbF6FG1wFZa36LpeuG98a__YYXpdHAkdTMrKZY%3D&alr=yes&sig=AOq0QJ8wRQIhAO5OnQZTy3f4l9cJNkfic6ERthTVI-US9NWueFI-3QpuAiAAn619SGC4qj-elRd1l02yqX7bWQMzmJIxHS0rcVwBEw%3D%3D


Type: video/webm; codecs="vp9", W×H 1280×720 720P60, Fps 60, ContentLength 8892222.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=302&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=video%2Fwebm&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=8892222&dur=232.333&lmt=1653317802719508&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgZ-ZVIogrraAhX6aqkx7S9vIUHPP9BzeJQkEq59fA3B8CIQDV37-iI2SRJLQ1975CEAE4w_A8B6dzZd7ustSv-Xod-w%3D%3D&alr=yes&sig=AOq0QJ8wRQIgb4kHYy7YE8AhpBGXevjmePSepCfeR7bYFuEKXRV-bzkCIQDyZNH-KmCAO4IAalc8PnfzjM1mw0YxiCPqfLTZmkxsOQ%3D%3D


Type: video/mp4; codecs="av01.0.08M.08", W×H 1280×720 720P60, Fps 60, ContentLength 11289786.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=398&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=video%2Fmp4&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=11289786&dur=232.333&lmt=1653309713746709&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4532434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAPMkD28iE2NdjPd73WiZ5oFfI3y2OaiF7L4-SZ4M1ffWAiEAmHUbYNFWAWmVz6JAUunobKhW5draj3mwEQ9lFNQBBTM%3D&alr=yes&sig=AOq0QJ8wRQIhALCX_YwW915e1DuAK1YndOfKU_Lv30xZRl2-ngqbFWPYAiAtbJUrpqGNdWY1k6D3pkbFjiwC-4D4SZW2j1djfmB-ZA%3D%3D


Type: video/mp4; codecs="avc1.4d401f", W×H 854×480 480P, Fps 30, ContentLength 2481594.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=135&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=video%2Fmp4&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=2481594&dur=232.333&lmt=1653309700663388&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgNB92ms0LEfTlpAwju0qgJurR0GqmlkdO6hMpo034XLACIGt30-bSwG4JHdI-viohKQynmh4rFG7iogjMFi8FgdnZ&alr=yes&sig=AOq0QJ8wRQIhANCo0BJ8pFh5cGrTh1mWLDMpcngS5hGNznJkA9KALxwlAiBgMAlyw73hGxQi5LEhMWrEsOwW0IyL82783iEKE3YcRw%3D%3D


Type: video/webm; codecs="vp9", W×H 854×480 480P, Fps 30, ContentLength 4589130.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=244&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=video%2Fwebm&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=4589130&dur=232.333&lmt=1653318123622338&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgdUOBCEXQd-8rAlD5RHzp90mbm7Xkyo74pHu_Zt3Mi68CIDRjyKn6EKSKgzdPV45wyB1KgfHiyEQbBkMQfLyV5_1t&alr=yes&sig=AOq0QJ8wRAIgJ0W0NCECIK1OfLSw8L6P0epbgz7vSNnK1_oknswEBPkCIG7NmBW9W7OaSERSPhnhOyO-SPVPsAKQlUDFtZNsVXHV


Type: video/mp4; codecs="av01.0.04M.08", W×H 854×480 480P, Fps 30, ContentLength 4808813.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=397&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=video%2Fmp4&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=4808813&dur=232.333&lmt=1653309418379607&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4532434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgZBmgm4gd9yw6JukqNq57FyIoxAz5A-fsNu19yD8uxKwCIGo46ZKDGtGfFyyq7A7YZbkemayqmM9he0GO3TA2thM8&alr=yes&sig=AOq0QJ8wRQIhAIpj5Mq2V5YbLMtP8oAuTqQ6qAO0cCWOG1HXPnkKnX7-AiAuFDtptbygvzXMtOPk5Z0rs4TJTNxoRc3OtsbBJHQ5kg%3D%3D


Type: video/mp4; codecs="avc1.4d401e", W×H 640×360 360P, Fps 30, ContentLength 1837997.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=134&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=video%2Fmp4&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=1837997&dur=232.333&lmt=1653309676339181&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhALsAxGF3xKFY0YxL77-0Op0jTEJ2X1nZ1D5yeu46hfraAiAA24KUPUeQcmO5g9syFPFTIyZI5rmWoU5WpIqfEnE4Gw%3D%3D&alr=yes&sig=AOq0QJ8wRQIgFuIRXKSd0y7IVPFvMmRb4SfDqgcGY6CvfzN9OEvjjVQCIQDNMoj0rOrxcG1dWTGeoOW2pTfCUkOGlZTQiGgcORhMsg%3D%3D


Type: video/webm; codecs="vp9", W×H 640×360 360P, Fps 30, ContentLength 3351050.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=243&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=video%2Fwebm&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=3351050&dur=232.333&lmt=1653318182166693&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgXX8umL_AWOgeZ_5ip-34wCi9WS7lAO604_8wf__ZOwcCIQDwIL8YDNzYeO_Uzxue-AnDWA-vLdjRyaUcM8dWCTeAcQ%3D%3D&alr=yes&sig=AOq0QJ8wRQIhALZmVPBJ7vTOPcXXFjw3g789BXyBiwLHVCGAtm2VJn6TAiAg72NF7kCzHuVnlh_OjWf-sfuBqSnQROQ_f4fAm6ugPw%3D%3D


Type: video/mp4; codecs="av01.0.01M.08", W×H 640×360 360P, Fps 30, ContentLength 3175510.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=396&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=video%2Fmp4&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=3175510&dur=232.333&lmt=1653309368223279&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4532434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAMqEXJPfG8hWUch-FMizSgpHsAJ_fE8qO-xmsc5r9ip_AiEAg36C_quF2rlyA-YfiKeqFWFQ7t1NcqdMntYRXgT4sug%3D&alr=yes&sig=AOq0QJ8wRAIgZADLXd3MjPdmS90-RDKLm5Ued4NfFoDDRnm541waC1ECIDC83A6VmwuxB3ZYqEjpoHUIvOg6hbYVsYsmgLRVXDAl


Type: video/mp4; codecs="avc1.4d4015", W×H 426×240 240P, Fps 30, ContentLength 1131067.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=133&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=video%2Fmp4&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=1131067&dur=232.333&lmt=1653309670774239&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAO1E8GGhVdRn8iQBRalF9LqAN2JsWW5XgMHBr5X9od_fAiEAjl4DdOsyvUiT01MhmEt6hllEoUE75yD5StrrCjfKSMg%3D&alr=yes&sig=AOq0QJ8wRQIhALNhGsf4FUpfdjwTbLvYETobWJukbY5uHZSA4gkPotc_AiBsrMcPzuUEkat1Iv-kzpub6y-ER_Cy4HEBmx9GyHBWAA%3D%3D


Type: video/webm; codecs="vp9", W×H 426×240 240P, Fps 30, ContentLength 2204153.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=242&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=video%2Fwebm&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=2204153&dur=232.333&lmt=1653318158908890&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhANO0IiytkoF7y2xXYZSHjalzdBARtf2pbsPBMCfxI6QZAiAlX696UZDSPKuFTKhoD-LY7pFqkUZLnu7IY8alJkqMUQ%3D%3D&alr=yes&sig=AOq0QJ8wRgIhANxClKjQOe57g5uzBPhRfnZE9GDXS7PST4h1GW2enkIbAiEAqwFY37nRCQuS8_wIgo9tTM_dmkKbRjpDSTA80Kso2E8%3D


Type: video/mp4; codecs="av01.0.00M.08", W×H 426×240 240P, Fps 30, ContentLength 2073347.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=395&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=video%2Fmp4&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=2073347&dur=232.333&lmt=1653309353228365&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4532434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAM1PLEnbz36R2QRj4SLs87yV1hnOTE0yQKmdIjEC74dlAiADaURJa5iLlstFijlTl_piwIdjRC-ogMdw__ee5uevtg%3D%3D&alr=yes&sig=AOq0QJ8wRQIhAK20O44vphCtc6SnH7OCkKvYwoiVTnJRq5TwfDptE9VmAiBqyDRJfHT90I49Wib55hbF0iE9y7xPy0ArXgEHrkMsNg%3D%3D


Type: video/mp4; codecs="avc1.4d400c", W×H 256×144 144P, Fps 30, ContentLength 707892.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=160&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=video%2Fmp4&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=707892&dur=232.333&lmt=1653309692268758&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAJeRjDHPa14JBj1b2eeM6n2JHrLtbi1C6ydi3YkiwL5TAiB9JsED7mTaHbMZuRu7F4ZWG_jc2UPVBHl0T-jx4xj2_Q%3D%3D&alr=yes&sig=AOq0QJ8wRAIgG2DZ3tW48dC3NDJUURzEbFoJjNXmEN27VQQo5J-X6wkCICHYilksk0hXZFLvvf1oKaSon6gIVSSOhraoAE1VrlrU


Type: video/webm; codecs="vp9", W×H 256×144 144P, Fps 30, ContentLength 1780751.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=278&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=video%2Fwebm&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=1780751&dur=232.333&lmt=1653318122544365&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAMF241RJnJBkQ2_w_h8e-6hTgyAAvWCD7Qn-o-8AciXeAiEAgKaEOWkSdJOdkMr9ckMXumhC4vBqrd-OkoejoGY3sVE%3D&alr=yes&sig=AOq0QJ8wRAIgebMTuiQMQtLlc6GhZX57_ZBufSv_M8IuBug3lCuF05UCIDT_SiQX72vo0YO4UQRCNSxE22TPxWOndBe69O0horCO


Type: video/mp4; codecs="av01.0.00M.08", W×H 256×144 144P, Fps 30, ContentLength 1596870.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=394&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=video%2Fmp4&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=1596870&dur=232.333&lmt=1653309352562251&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4532434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAP7IAkuGRNMmgDdKtNASoDYod38pgh83Hp_nwBl4h6irAiEA9jeHGZc4yU6EYi7o0VK6d0OTOR_A1ZMEYYTl7qxtr04%3D&alr=yes&sig=AOq0QJ8wRQIhAJhqlQBUrSgcM5ETaJlf-GZuyjDpBJe_dssYXK8Td1auAiBOXHv3Y-_mO74PycRUtIo8Y4EZT7phVFpxIFcCSCdJYg%3D%3D


Type: audio/mp4; codecs="mp4a.40.2", Bitrate 130494, Rate 44100, Channels 2, Quality AUDIO_QUALITY_MEDIUM, ContentLength 3762144.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=140&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=audio%2Fmp4&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=3762144&dur=232.385&lmt=1653307660360778&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4532434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAMbX47e7m6LOS_CwdVBZ502XNpxkws_4z7SuZJrqNzDDAiEAswgF8Ntih1eYneppG_MCpLp_pwoX0uQulSBAEQTDyl8%3D&alr=yes&sig=AOq0QJ8wRQIga2EBIgG56cCrWZKRi2lHnG629YWokiIhgCvIlLuKcfkCIQD2WO6B7KxSuvjRl0s-C87Nnb9A-zblSGzPfVQxaATgRA%3D%3D


Type: audio/webm; codecs="opus", Bitrate 60499, Rate 48000, Channels 2, Quality AUDIO_QUALITY_LOW, ContentLength 1461482.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=249&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=audio%2Fwebm&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=1461482&dur=232.361&lmt=1653307657068312&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4532434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgTia-lAcu6ib2VU1wvTNH2kulOCkELcX99UGQCiYeIX0CICkrjKEJlEQUP7ll0EGACdrzUrMTIaKZxVs2jQ2X_AwV&alr=yes&sig=AOq0QJ8wRQIhAIfg22KuCVXfaq0dZzqaX9k72P783XXBQG7ooi9GiEGnAiA6-izWn1ACDx26tQFFYqdc0VfXYjgPTcxsCsx06jx7nQ%3D%3D


Type: audio/webm; codecs="opus", Bitrate 79303, Rate 48000, Channels 2, Quality AUDIO_QUALITY_LOW, ContentLength 1936759.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=250&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=audio%2Fwebm&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=1936759&dur=232.361&lmt=1653307657509294&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4532434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgMbzW3JItOLJIlJm0NheMQEErRbzemFk8eqduZ2atTwwCIQCdutWcxYbpSN27nzjsjWBq8RP7uJBL8f2TS8gxWXWQUw%3D%3D&alr=yes&sig=AOq0QJ8wRAIgbZUBiK5hUDlLHydNK-KD7KUGhww8SJmIFcYfNGuxtVUCIGHINWlxP_Tb_AxlbzyuISRvFlceqyu0Gh3-G0oyHKeX


Type: audio/webm; codecs="opus", Bitrate 150852, Rate 48000, Channels 2, Quality AUDIO_QUALITY_MEDIUM, ContentLength 3822436.
https://rr5---sn-ipoxu-u2x6.googlevideo.com/videoplayback?expire=1667234368&ei=4KVfY9r8EZyM0-kPyNuamAw&ip=2001%3Ab011%3A7006%3A3d2e%3Aa0fd%3A500a%3Ac32%3A8507&id=o-AIgclijYWDEMrHJc9rXCX9HoFvuybfcqZ7-1IecQTrL9&itag=251&source=youtube&requiressl=yes&mh=g5&mm=31%2C29&mn=sn-ipoxu-u2x6%2Csn-un57ene6&ms=au%2Crdu&mv=m&mvi=5&pl=54&gcr=tw&initcwndbps=966250&vprv=1&mime=audio%2Fwebm&ns=BmS_H0qdZvHYp-y8PHC3cB0I&gir=yes&clen=3822436&dur=232.361&lmt=1653307657229968&mt=1667212393&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4532434&n=iR5J8Vb60GTNUmn2&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgVqMyHV-sL224FpLw4NJgGmshOYgV90gz4fl57bH7VKUCIDHwJUMGEQYqfbn3Hyb2HYdH4znW00JCTdqlpq2Wyg__&alr=yes&sig=AOq0QJ8wRQIhAMhXA-kNvmd-sYPyEsv2UcOakvTwiQFSwEUvzHZaL8KiAiBeynzASXwLf6TvljrZtKRpCRebWscJDg92fHjwYF2hEw%3D%3D

complete
```
Should you use this to download youtube video?<br>
A: No, use youtube-dl instead, because I may not maintain this project.

This project can do what?<br>
A: This project simply show you how to download youtube video use python.
This project include Decrypt_2022_10_29_zh_TW class that be used to decrypt signature cipher.

## How does this project work?
1. Get the youtube page source code.
2. Get video name, base.js url, video infomation from source code. The base.js is the script including decrpyt function, in the different video or time may have different base.js url in source code, and its decrypt function will have different name, argument, sequence, but same content inner function.
3. Extract the decrypt function inner base.js by using regex.
4. If this video is protected, use decrypt function to decrypt the signature cipher and add it to video url that both have been finded in video information.
5. Downloading video and audio by url use thread and range.
6. Using FFmpeg transform their format to mp4 (h264,aac).
7. Complete

## References:<br>
[https://github.com/SurpassHR/Youtube_SignatureCipher_Decryptor](https://github.com/SurpassHR/Youtube_SignatureCipher_Decryptor)<br>
[https://github.com/streamlink/streamlink/blob/master/src/streamlink/plugins/youtube.py](https://github.com/streamlink/streamlink/blob/master/src/streamlink/plugins/youtube.py)<br>
[https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/extractor/youtube.py](https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/extractor/youtube.py)<br>
[https://stackoverflow.com/a/68492807](https://stackoverflow.com/a/68492807)

Also see:
[https://stackoverflow.com/a/74223304/19470749](https://stackoverflow.com/a/74223304/19470749)

## Write Downloading Code:

If you want to write this like me, first go youtube website seeing browser developer tools network, second go to see the youtube website source code, third go to see youtube base.js source code, you also need to use find function, set breakpoint in base.js. It is not needing that see the full source code, just roughly view to find some interesting infomation like googlevideo.com.

## Decrypt SignatureCipher:

If you want to decrypt signatureCipher, there is one thing to attention. When you get the decrypt function in base.js, that's not mean you get the currect decrypt function, because in different youtube video may have different base.js url and different decrypt function name, sequence, argument in it. If use wrong decrypt function or give full argument but some is error, rr$d---sn-$s-$s.googlevideo.com will keep 403 forbidden. If not give necessary parameter, it will response "404 Not Found. That’s an error". The real decrypt function in different base.js is not much different, it only change name, rearrange the real decrypt function, and replace the arguments that the real decrypt function will use (int). When you use the currect decrypt function, it will successfully get the video.<br>
When you want to find the decrypt function in base.js, the key words are: split(""), encodeURIComponent, decodeURIComponent, signature, sig.<br>
In 2022.10.$day, it format like that:

```javascript
//Common
//Rwa(a){a.split("")...}
Rwa=function(a){a=a.split("");RB.ss(a,4);RB.jM(a,6);RB.jM(a,45);RB.e0(a,3);return a.join("")};
var RB={ss:function(a){a.reverse()},
jM:function(a,b){var c=a[0];a[0]=a[b%a.length];a[b%a.length]=c},
e0:function(a,b){a.splice(0,b)}};

//Qwa(a){a.split("")...}
Qwa=function(a){a=a.split("");PB.Co(a,14);PB.Co(a,14);PB.Zo(a,56);PB.GZ(a,2);return a.join("")};
var PB={Co:function(a,b){var c=a[0];a[0]=a[b%a.length];a[b%a.length]=c},
Zo:function(a){a.reverse()},
GZ:function(a,b){a.splice(0,b)}};

//Common
QE = function(a, b, c) {  //### This Function will decrypt signatureChiper ###//
    b = void 0 === b ? "" : b;
    c = void 0 === c ? "" : c;
    a = new g.SB(a,!0);
    a.set("alr", "yes");
    c && (c = Rwa(decodeURIComponent(c)), //### This Line will decrypt signatureChiper ###//
    a.set(b, encodeURIComponent(c)));
    return a
}

QE = function(a, b, c) {  //### This Function will decrypt signatureChiper ###//
    b = void 0 === b ? "" : b;
    c = void 0 === c ? "" : c;
    a = new g.SB(a,!0);
    a.set("alr", "yes");
    c && (c = Qwa(decodeURIComponent(c)), //### This Line will decrypt signatureChiper ###//
    a.set(b, encodeURIComponent(c)));
    return a
}

RE=function(a,b,c){b=void 0===b?"":b;c=void 0===c?"":c;a=new g.SB(a,!0);a.set("alr","yes");c&&(c=Rwa(decodeURIComponent(c)),a.set(b,encodeURIComponent(c)));return a};
```
What you can search in base.js is "{a=a.split("")", and continue search the function name inner just find.

You can also see the details in:<br>
https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/extractor/youtube.py#L1403

## Base.js

Base.js is the script which be use to decrypt signature cipher. 

Format:
```
Windows:

https://www.youtube.com/s/player/${Js_Id}/player_ias.vflset/${Country}/base.js
Android:

https://www.youtube.com/s/player/${Js_Id}/player-plasma-ias-tablet-${Country}/base.js
```
Here are some base.js url I catched: (2022/10/${day})<br>
[https://www.youtube.com/s/player/4bbf8bdb/player_ias.vflset/zh_TW/base.js](https://www.youtube.com/s/player/4bbf8bdb/player_ias.vflset/zh_TW/base.js)
[https://www.youtube.com/s/player/24c6f8bd/player_ias.vflset/zh_TW/base.js](https://www.youtube.com/s/player/24c6f8bd/player_ias.vflset/zh_TW/base.js)
[https://www.youtube.com/s/player/64588dad/player_ias.vflset/zh_TW/base.js](https://www.youtube.com/s/player/64588dad/player_ias.vflset/zh_TW/base.js)
[https://www.youtube.com/s/player/4bbf8bdb/player-plasma-ias-tablet-zh_TW.vflset/base.js](https://www.youtube.com/s/player/4bbf8bdb/player-plasma-ias-tablet-zh_TW.vflset/base.js)
[https://www.youtube.com/s/player/24c6f8bd/player-plasma-ias-tablet-zh_TW.vflset/base.js](https://www.youtube.com/s/player/24c6f8bd/player-plasma-ias-tablet-zh_TW.vflset/base.js)
[https://www.youtube.com/s/player/64588dad/player-plasma-ias-tablet-zh_TW.vflset/base.js](https://www.youtube.com/s/player/64588dad/player-plasma-ias-tablet-zh_TW.vflset/base.js)
