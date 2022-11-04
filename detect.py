import speech_recognition as sr
import re

if __name__=='__main__':

    count=0

    try:
        while True:
            r = sr.Recognizer()
            
            with sr.Microphone() as source:
                print('음성을 입력하세요.')
                audio = r.listen(source)
                try:
                    stt=r.recognize_google(audio, language='ko-KR')
                    print('음성변환 : ' + stt)
                    count+=len(re.findall('그죠',stt))
                    print('현재까지 그죠 {}회 반복'.format(count))
                except sr.UnknownValueError:
                    print('오디오를 이해할 수 없습니다.')
                except sr.RequestError as e:
                    print(f'에러가 발생하였습니다. 에러원인 : {e}')
                    
    except KeyboardInterrupt:
        pass