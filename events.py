from fbchat import Client
from fbchat.models import *
from datetime import datetime
import time
import requests
import json

def startEventListining(email, password, session_cookies=None):
    
    class events(Client):
        #handel events from group chat
        def onPeopleAdded(self, added_ids, author_id, thread_id, **kwargs):
          
          if author_id != author_id:
            for added_id in added_ids:                
                
                user = self.fetchUserInfo(added_id)[added_id]
                name = user.name
                
                group_info = self.fetchGroupInfo(thread_id)
                
            if thread_id in group_info:
                participants = group_info[thread_id].participants
                participant_count = len(participants)
               
                            
                
                message = f"Welcome to the group, {name}!\nID: {added_id}\nJoined at: {datetime.now()}\nmembers:{participant_count}"
                self.send(Message(text=message), thread_id=thread_id, thread_type=ThreadType.GROUP)
                
                
                group_info = self.fetchGroupInfo(thread_id)
            if thread_id in group_info:
                participants = group_info[thread_id].participants
               
        def onPersonRemoved(self,mid=None, removed_id=None, author_id=None, thread_id=None, ts=None, msg=None):
                user = self.fetchUserInfo(removed_id)[removed_id]
                name = user.name
                author= self.fetchUserInfo(author_id)[author_id]
                author_name = author.name
                
                msg=f"""REMOVAL UPDATE\n\nremoved user:{name}\n\nremoved by:{author_name}\n\n{datetime.now()}"""
                self.send(Message(text=msg), thread_id=thread_id, thread_type=ThreadType.GROUP)
                        
                          
        def onAdminAdded(self,mid=None, added_id=None, author_id=None, thread_id=None, thread_type=ThreadType.GROUP, ts=None, msg=None):
           
                user = self.fetchUserInfo(added_id)[added_id]
                name = user.name
                author= self.fetchUserInfo(author_id)[author_id]
                author_name = author.name
                
                msg=f"""
                ADMIN UPDATED\nnew admin:{name}\nadded by:{author_name}\n\n{datetime.now()}
                """
                self.send(Message(text=msg), thread_id=thread_id, thread_type=ThreadType.GROUP)
                
 
                
        def onAdminRemoved(self,mid=None, removed_id=None, author_id=None, thread_id=None, thread_type=ThreadType.GROUP, ts=None, msg=None):  
                user = self.fetchUserInfo(removed_id)[removed_id]
                name = user.name
                author= self.fetchUserInfo(author_id)[author_id]
                author_name = author.name
                
                msg=f"""
                ADMIN UPDATED\admin removed:{name}\n removed by:{author_name}\n\n{datetime.now()}
                """
                self.send(Message(text=msg), thread_id=thread_id, thread_type=ThreadType.GROUP)
                                                           

        def onApprovalModeChange(self,mid=None, approval_mode=None, author_id=None, thread_id=None, thread_type=ThreadType.GROUP, ts=None, msg=None):   
            author= self.fetchUserInfo(author_id)[author_id]
            author_name = author.name
                
            msg=f"""
                APPRPROVAL UPDATE\n\nstatus:{approval_mode}\n\nby:{author_name}\n\n{datetime.now()}
                """
            self.send(Message(text=msg), thread_id=thread_id, thread_type=ThreadType.GROUP)

                                    
        

        def onNicknameChange(self,mid=None, author_id=None, changed_for=None, new_nickname=None, thread_id=None, thread_type=ThreadType.USER, ts=None, metadata=None, msg=None):
            
            user = self.fetchUserInfo(changed_for)[changed_for]
            name = user.name
            author= self.fetchUserInfo(author_id)[author_id]
            author_name = author.name
                
            msg=f"""
                NICKNAME UPDATED\n\nnickname of:{name}\n\nnickname:{new_nickname}\n\nby:{author_name}\n\n{datetime.now()}
                """
            self.send(Message(text=msg), thread_id=thread_id, thread_type=ThreadType.GROUP)
                                         
 

        def onTitleChange(self,mid=None, author_id=None, new_title=None, thread_id=None, thread_type=ThreadType.USER, ts=None, metadata=None, msg=None):
            author= self.fetchUserInfo(author_id)[author_id]
            author_name = author.name
            msg=f"""TITLE/GROUP NAME UPDATE\n\n current name:{new_title}\n\nby:{author_name}\n\n{datetime.now()}"""
            self.send(Message(text=msg), thread_id=thread_id, thread_type=ThreadType.GROUP)
                 
        def onEmojiChange(self,mid=None, author_id=None, new_emoji=None, thread_id=None, thread_type=ThreadType.USER, ts=None, metadata=None, msg=None):         
            author= self.fetchUserInfo(author_id)[author_id]
            author_name = author.name
            msg=f"""EMOJI UPDATE\n\ncurrent emoji:{new_emoji}\n\nby:{author_name}\n\n{datetime.now()}"""
            self.send(Message(text=msg), thread_id=thread_id, thread_type=ThreadType.GROUP)
                 
            
        def onColorChange(self,mid=None, author_id=None, new_color=None, thread_id=None, thread_type=ThreadType.USER, ts=None, metadata=None, msg=None): 
            author= self.fetchUserInfo(author_id)[author_id]
            author_name = author.name
            msg=f"""COLOR/THEME UPDATED\n\n current color/theme:{new_color}\n\nby:{author_name}\n\n{datetime.now()}"""
            self.send(Message(text=msg), thread_id=thread_id, thread_type=ThreadType.GROUP)
            
    
        # handle msg request and friend request                               
        def onPendingMessage(self,thread_id=None, thread_type=None, metadata=None, msg=None):
              
              self.send(Message(text=f"""ohayo!!!"""), thread_id=thread_id, thread_type=thread_type)
              
                
              thread_info = self.fetchThreadInfo(thread_id)[thread_id]
              group_name = thread_info.name 

              self.send(Message(text=f"""connected successfully to {group_name}"""), thread_id=thread_id, thread_type=thread_type)
                
              self.changeNickname('bot (no prefix)',user_id=self.uid,thread_id=thread_id,thread_type=thread_type)

                
            
        def onFriendRequest(self,from_id=None, msg=None):
                
                self.send(Message(text="""friend request received"""), thread_id=from_id)
                
        
        
         #handle chats 
    def onMessage(self, mid=None, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
            
            message_object
            
            def sendMsg():
                if author_id != self.uid:
                    self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)
    
            try:
                msg = str(message_object).split(",")[15][14:-1]
                print(msg)
                message_object.split(",")[0]
                if "//video.xx.fbcdn" in msg:
                    msg = msg
                else:
                    msg = str(message_object).split(",")[19][20:-1]
            except:
                try:
                    msg = message_object.text.lower()
                    print(msg)
                except:
                    pass
    
            if author_id != self.uid:
                lower_msg = msg.lower()
                
                if lower_msg.startswith('ai'):
                    
                    reply="asking ai"
                    sendMsg()
                    
                    response=r.get('https://sim.ainz-project.repl.co/others/gpt?prompt=hi how are you').json()
                    reply=response['result']
                    sendMsg()
                                
        
                elif lower_msg.startswith("bard"):
                        
                        try:
                            if lower_msg =="bard":
                                reply="usage:bard <ask>"
                                sendMsg()
                            else:
                                reply="asking bard"
                                sendMsg()
                                q=lower_msg.replace("bard ","").replace(" ","")
                                url=f"https://api.heckerman06.repl.co/api/other/bard-ai69?response={q}"
                                
                                c=requests.get(url)
                                
                                links=[]
                                text=c.json()["content2"]
                                if c.json()["content"]=="No image found":
                                    reply=text
                                    sendMsg()
                                else:
                                    for v in c.json()["content"]:
                                         links.append(v[0][0])
                                    self.sendRemoteFiles(links, message=text, thread_id=thread_id, thread_type=thread_type)

                                                                     
                        except Exception as e :
                                     reply=e
                                     sendMsg()   
                                     
                                                       
                elif lower_msg.startswith("pinterest"):
                    reply="searching pinterest"
                    sendMsg()
                    try:
                            a = lower_msg
                            removepre = a.replace("pinterest ", "")
                            sp = removepre.split(" ")
                            n = int(sp[len(sp) - 1].replace("-", ""))
                            rvc = removepre.replace(sp[len(sp) - 1], "")
                            url = f"https://sim.ainz-project.repl.co/search/pinterest?search={rvc}"
                            res = requests.get(url).json()["data"][:n]
                            self.sendRemoteFiles(res, message=lower_msg, thread_id=thread_id, thread_type=thread_type)
                    except Exception as e:
                        reply = e
                        sendMsg()
                        
                elif   lower_msg.startswith('brainly'):
                            reply="searching brainly"
                            sendMsg()
                            v=lower_msg.replace('brainly','')
                            response=requests.get('https://bly.jemcarl.repl.co/brainly?q='+q).text.replace('<br />','\n')
                            html_content = response
                            soup = BeautifulSoup(html_content, 'html.parser')
                            text = soup.get_text()
                            reply=text
                            sendMsg()
                            
                elif lower_msg.startswith('lyrics'):
                             reply="searching lyrics"
                             sendMsg()
                             v=lower_msg.replace('lyrics','').replace(' ','')
                             full=''
                             v = requests.get(f"https://api.heckerman06.repl.co/api/other/lyrics2?song={t}").text
                             v=eval(v)
                             full+='title:'+v['title']+'\n'
                             full+='artist:'+v['artist']+'\n'
                             full +='lyrixs:'+v['lyrics']+'\n'
                             reply=full
                             sendMsg()               
                 
    bot = events(email, password, session_cookies=session_cookies)
    
    
    try:
        print('trying to start bot....')
        bot.listen()
    except Exception:
        print('cannot startbot please try again after 3-5 seconds')
