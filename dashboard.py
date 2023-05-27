import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Olympics Analysis Web App",
    page_icon="https://img.freepik.com/premium-vector/sport-icon-design_24908-6325.jpg",
    layout="wide",
    initial_sidebar_state="expanded",

)

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# remove top spacing
st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom:0rem;
                }
        </style>
        """, unsafe_allow_html=True)

# bottom to top button
st.markdown("<div id='LinkToTop'></div>", unsafe_allow_html=True)


def navigation_bar():
    with st.container():
        selected = option_menu(
            menu_title=None,
            options=["Home", "About", "Summer Olympics", 'Winter Olympics', 'Overall Analysis'],
            icons=['house', 'people', "list-task", "map", 'flag'],
            menu_icon="cast",
            orientation="horizontal",
            styles={
                "nav-link": {
                    "text-align": "center",
                    "--hover-color": "#eee",
                    "font-size": "19px",
                    "font-family": "times new roman",
                }
            }
        )

        if selected == "Home":
            st.markdown("""
                        <style>
                            img{
                            border: 1px solid  silver;
                            }
                        </style>    
                        """, unsafe_allow_html=True)
                # Flag Image

            st.markdown(
                "<center>" '<img src= "https://r0.wallpaperflare.com/path/662/933/133/competition-ring-athlete-sport-23aac30a2865ec6d0802fe23a118c251.jpg?timestamp=1682158950658" style="width:100%; height: 27rem;">',
                unsafe_allow_html=True)

            st.markdown("""
                        <style>
                            .oly-ana {
                                padding-top: 30px;
                                font-size:60px !important;
                                color: #0099e6;
                                text-align:center;
                                font-family: times new roman;
                            }
                        </style>
                        """, unsafe_allow_html=True)
            st.markdown('<p class="oly-ana"><b>Olympics Analysis</p>', unsafe_allow_html=True)

            st.markdown("""
                        <style>
                            .detail {
                                font-size:20px !important;
                                color: #595959;
                                text-align: justify;
                                font-family: times new roman;
                            }
                        </style>
                        """, unsafe_allow_html=True)
            st.markdown(
                "<p class='detail'> The modern Olympic Games or Olympics are the leading international sporting events featuring summer and winter sports competitions in which thousands of athletes from around the world participate in a variety of competitions. The Olympic Games are considered the world's foremost sports competition with more than 200 teams, representing sovereign states and territories, participating. </p>",
                unsafe_allow_html=True)
            st.markdown(
                "<p class='detail'>Olympism, the spirit of the Olympic Games advocated by Coubertin, is “The elevation of the mind and soul, overcoming differences between nationalities and cultures, embracing friendship, a sense of solidarity, and fair play; ultimately leading to the contribution towards world peace and the betterment of the world. “ This philosophy has been passed down, unchanged, to this day, so Coubertin is considered to be the “Father of the modern Olympics”.</p>",
                unsafe_allow_html=True)

            st.markdown("""
                        <style>
                            .sltctg{
                                font-size:50px !important;
                                color: #0099e6;
                                text-align:center;
                                font-family: times new roman;
                            }
                        </style>
                        """, unsafe_allow_html=True)
            st.markdown('<h1 class="sltctg"><b>Select Your Category</b> </h1>', unsafe_allow_html=True)

            st.markdown("""
                            <style>
                            .ssn-name{
                                font-family: times new roman;  
                                color: #ff8000;
                                padding-bottom: 3rem;

                            }
                            </style>
                            """, unsafe_allow_html=True)

            st.markdown("""
                            <style>
                                .ssn-info{
                                    width: 100%;
                                    font-size:19.8px !important;
                                    color: black;
                                    text-align: justify; 
                                    font-family: times new roman; 
                                    padding-bottom: 3rem;   
                            }
                            </style>
                            """, unsafe_allow_html=True)

            # summer olympics
            st.markdown("<center><h1 class='ssn-name'>Summer Olympics</h1>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.write(
                    "<center>" '<a href="https://summer-analysis-vo9q.onrender.com" target="_blank"> <img src= "https://e1.pxfuel.com/desktop-wallpaper/204/776/desktop-wallpaper-boxing-ring-virtual-set-boxing-ring-background.jpg" style="width:100%;height:280px;" > </a>',
                    unsafe_allow_html=True)
            with col2:
                st.markdown(
                    '<p class="ssn-info">The inaugural Games of the modern Olympics were attended by as many as 280 athletes, all male, coming from 12 countries. The athletes competed in 43 events covering athletics (track and field), cycling, swimming, gymnastics, weightlifting, wrestling, fencing, shooting, and tennis. The Summer Olympic Games, also known as the Games of the Olympiad, normally held once every four years. The first Summer Olympic Games, were held in Athens, Greece, 1896. The 2024 Games were scheduled to be held in Paris, and the 2028 Games were scheduled to be held in Los Angeles. </p>',
                    unsafe_allow_html=True)

            # winter olympics
            st.markdown('<center><h1 class="ssn-name">Winter Olympics</h1>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.write(
                    "<center>" '<a href="https://winter-analysiis.onrender.com", target="_blank"> <img src= "https://www.usfigureskating.org/sites/default/files/styles/flexible_hero_image/public/media-library/GettyImages-1367630025.jpg?itok=oUjx_5nT" style="width:100%;height:280px;" > </a>',
                    unsafe_allow_html=True)
            with col2:
                st.markdown(
                    '<p class="ssn-info">Although some skating events were included in the 1908 and 1920 Games, it was not until 1924 that the Winter Games were accepted as a celebration comparable to the Summer Games and given the official blessing of the International Olympic Committee (IOC). The Winter Olympic Games is a major international multi-sport event held once every four years for sports practiced on snow and ice. The first Winter Olympic Games, were held in Chamonix, France, 1924. The 2018 Winter Olympics were held in P’yŏngch’ang, South Korea, and the 2022 Winter Games were held in Beijing.</p>',
                    unsafe_allow_html=True)

            # overall analysis
            st.markdown('<center><h1 class="ssn-name">Overall Analysis</h1>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.write(
                    "<center>" '<a href="https://overall-analysis-dclg.onrender.com", target="_blank"> <img src= "https://e0.pxfuel.com/wallpapers/121/708/desktop-wallpaper-3d-political-world-map-blue-brickwall-map-of-world-countries-creative-world-maps-3d-art-3d-world-map-world-map-concepts-world-map-with-flags.jpg" style="width:100%;height:280px;" > </a>',
                    unsafe_allow_html=True)

            with col2:
                st.markdown(
                    '<p class="ssn-info">The ideas and work of several people led to the creation of the modern Olympics. The best-known architect of the modern Games was Pierre, baron de Coubertin, born in Paris on New Year’s Day, 1863. At age 24 Coubertin decided that his future lay in education, especially physical education. The Modern Olympic Games are normally held every four years, and since 1994, have alternated between the Summer and Winter Olympics every two years during the four-year period.The Olympic Games have come to be regarded as the world’s foremost sports competition.</p>',
                    unsafe_allow_html=True)


            # create a container for the footer
            footer_container = st.container()

            # set the CSS style for the container to make it fixed and position it at the bottom of the page
            footer_container.markdown(
                """
                <style>
    
                /* Adjust the font size on smaller screens */
                    @media only screen and (max-width: 600px) {
                        body{
                            font-size: 16px;
                        }
                    }
    
                    /* Adjust the layout on smaller screens */
                    @media only screen and (max-width: 600px) {
                        body{
                            display: flex;
                            flex-direction: column;
                        }
                    }
    
                .footer {
                    position: float;
                    width: 100%;
                    background: rgb(32,40,38);
                    background: linear-gradient(25deg, rgba(32,40,38,1) 13%, rgba(42,91,91,1) 28%, rgba(73,46,91,1) 51%, rgba(44,75,80,1) 81%, rgba(76,49,78,1) 95%);
                    padding: 12px;
                    text-align: center;
                    font-size: 17px;
                    color: black;
                    border-top: 1px solid #ddd;
                    padding-bottom:.5rem;
                }
    
                .footer p{
                    text-align:center;
                    padding-top:0px;
                    color:#a6a6a6;
                    font-family: times new roman;
                    font-size: 17px; 
    
                }
    
                .footer1 a {
                    color: #ccffff;
                    font-size: 16px;
    
    
                }
    
                .footer1 h4{
                                font-family: times new roman;  
                                color: white;
                                padding-bottom: 30px;
                                padding-top: 38px;
                            }
    
                .footer1{
                    position: float;
                    width: 100%;
                    background: rgb(32,40,38);
                    background: linear-gradient(25deg, rgba(32,40,38,1) 13%, rgba(42,91,91,1) 28%, rgba(73,46,91,1) 51%, rgba(44,75,80,1) 81%, rgba(76,49,78,1) 95%);
                    padding: 7px;
                    text-align: center;
                    font-size: 17px;
                    color: white;   
                }
    
                .footer1 p{
                    text-align:center;
                    margin-left:9rem;
                    margin-right: 9rem;
                    color:#d9d9d9;
                    font-family: times new roman;
                    font-size: 17px;  
    
                }
    
                hr{
                width:0px;
                }
                </style>
                """,
                unsafe_allow_html=True,
            )

            # add your footer content to the container
            with footer_container:
                st.markdown(
                    """ 
                    <div class ="footer1"><center>
                        <h4> <center> Contact Us </h4>
                        <div style="display: flex; flex-direction: column;">
                            <div style="display: flex;">
                                <div style="flex: 1; color:#d9d9d9;font-family: times new roman;">Isha Agarwal</div>
                                <div style="flex: 1; color:#d9d9d9;font-family: times new roman;">Pankhuri</div>
                                <div style="flex: 1; color:#d9d9d9;font-family: times new roman;">Madhav Agarwal</div>
                            </div>
                            <div style="display: flex;">
                                <div style="flex: 1;margin-top: 10px;"><a href="mailto:ishaagarwal179@gmail.com">ishaagarwal179@gmail.com</a></div>
                                <div style="flex: 1;margin-top: 10px;"><a href="mailto:pankhurigarg2001@gmail.com">pankhurigarg2001@gmail.com</a></div>
                                <div style="flex: 1;margin-top: 10px"><a href="mailto:madhav.ag56@gmail.com">madhav.ag56@gmail.com</a></div>
                            </div>
                            <div style="display: flex;">
                                <div style="flex: 1;margin-top: 10px;margin-bottom: 10px"><a href="https://www.linkedin.com/in/isha-agarwal-44120021a/">www.linkedin.com/in/isha-agarwal-44120021a</a></div>
                                <div style="flex: 1;margin-top: 10px"><a href="https://www.linkedin.com/in/pankhuri-613a-/">www.linkedin.com/in/pankhuri-613a-</a></div>
                                <div style="flex: 1;margin-top: 10px"><a href="https://www.linkedin.com/in/madhav-agarwal-b8130b221/">www.linkedin.com/in/madhav-agarwal-b8130b221</a></div>
                            </div>
                        </div>
                    </div>      
                    <div class="footer"><center>
                        <p><i>Powered by students of SRMSCET,Bareilly.</i> </p>
                        <p><i>Department of Computer Science and Engineering</i> </p>
                        <p><i>© Copyright 2023.</i> </p>
                        <p><i>All rights are reserved</i></p>
                        <p>• Privacy Policy &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Accessibility &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Sitemap  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  • Support</p>   
                        <p>© 2023 My Website</p>
                        <a target="_blank" title="Follow me on Twitter" href="https://twitter.com/login?lang=en"><img alt="Follow me on Twitter" src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Twitter_colored_svg-1024.png" style="width:40px;height:40px;border: 1.5px solid white; border-radius:20%; margin-left:.25rem;padding:2px;"></a>
                        <a target="_blank" title="Follow me on Facebook" href="https://www.facebook.com/PLACEHOLDER"><img alt="Follow me on Facebook" src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Facebook_colored_svg_copy-1024.png" style="width:40px;height:40px;border: 1.5px solid white; border-radius:20%; margin-left:.25rem;padding:4px;"></a>
                        <a target="_blank" title="Send message on WhatsApp" href="https://www.whatsapp.com/"><img alt="Send message on WhatsApp" src=" https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Whatsapp2_colored_svg-1024.png" style="width:40px;height:40px;border: 1.5px solid white; border-radius:20%; margin-left:.25rem;padding:4px;"></a>
                        <a target="_blank" title="Follow me on Instagram" href="https://www.instagram.com/"><img alt="Follow me on Instagram" src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Instagram_colored_svg_1-1024.png" style="width:40px;height:40px;border: 1.5px solid white; border-radius:20%; margin-left:.25rem;padding:4px;"></a>
                        <a target="_blank" title="Follow me on LinkedIn" href="https://in.linkedin.com/"><img alt="Follow me on LinkedIn" src=" https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-1024.png" style="width:40px;height:40px;border: 1.5px solid white; border-radius:20%;margin-left:.25rem;padding:4px;"></a>
                        <a target="_blank" title="Send message on Messenger" href="https://www.messenger.com/"><img alt="Send message on Messenger" src="https://cdn4.iconfinder.com/data/icons/social-media-2285/1024/logo-1024.png" style="width:40px;height:40px; border: 1.5px solid white; border-radius:20%; margin-left:.25rem;"></a>   
                    </div>
    
                    """,
                    unsafe_allow_html=True,
                )

        st.markdown("""
                                <style>
                                    .about{
                                        width: 100%;
                                        font-size:20px !important;
                                        color: black;
                                        text-align: justify; 
                                        font-family: times new roman; 
                                        padding-bottom: 1rem;   
                                    }
                                    .ab-name{
                                        font-size: 40px;
                                        font-family: times new roman;
                                        color: #0099e6;
                                    }
                                    a{
                                    text-decoration: none;
                                    }
                                </style>
                                """, unsafe_allow_html=True)
        if selected == 'About':

            st.markdown("<center><h1 class='ab-name'>About Olympics</h1>", unsafe_allow_html=True)
            st.markdown("<p class='about'>Olympics games are considered as one of the most prime events which provides a valid and common platform for players across different countries to show their talent and skills. Modern Olympic Games were originated by taking inspiration from Ancient Olympic Games held in Olympia, Greece from the 8th Century BC to the 4th Century AD. The following timeline outlines the main events in the history of Modern Olympic Games. The Olympics consists of various games (Approximately 45) in which players from various countries (Approx 205) participate to win a medal for their country.Olympic Games are considered the world's foremost sports competition with more than 200 teams, representing sovereign states and territories, participating. The Olympic Games are normally held every four years, and since 1994, have alternated between the Summer and Winter Olympics every two years during the four-year period.</p>", unsafe_allow_html=True)
            st.markdown("<center><h1 class='ab-name'>History of Olympics</h1>", unsafe_allow_html=True)
            st.markdown("""<p class='about'>The Olympic Games have a long and rich history, dating back to ancient Greece in the 8th century BCE. The Games were held every four years in Olympia, in honour of the god Zeus, and included various athletic events such as running, wrestling, and discus throwing. 
            The ancient Olympics continued for nearly 12 centuries until they were banned by Emperor Theodosius I in 393 CE, as part of his campaign to suppress pagan festivals.It was not until the late 19th century that the modern Olympics were founded by French educator Baron Pierre de Coubertin. 
            The first modern Olympic Games were held in Athens, Greece in 1896 and included nine sports with 241 athletes from 14 countries. Since then, the Olympics have been held every four years, except for during World War I and World War II. The number of sports and athletes has increased significantly, and the Games have become a major global event, with thousands of athletes from hundreds of countries competing in dozens of sports. The modern Olympics have faced various challenges and controversies over the years, including boycotts, doping scandals, and political tensions. However, the Games remain a symbol of international cooperation, sportsmanship, and athletic excellence, and continue to inspire millions of people around the world.</p>""",unsafe_allow_html=True)
            st.markdown("""<p class='about'> The Olympics are a global phenomenon, attracting athletes, spectators, and media coverage from around the world. One of the most significant changes in the history of the Olympics was the addition of women's events. At the first modern Olympics in 1896, women were not allowed to compete. It was not until the 1900 Games in Paris that women's events were included, with women competing in five sports: tennis, golf, croquet, equestrian, and sailing.
            Since then, the number of women's events has increased significantly, and women now compete in virtually every sport at the Olympics.Another major change has been the globalization of the Games. In the early years of the modern Olympics, most athletes were from Europe and North America. However, in recent decades, more and more athletes from Asia, Africa, and South America have competed, reflecting the growing internationalization of the sports world.In addition, the Olympics have become a major economic and political event. Hosting the Games is a significant investment for cities and countries, requiring the construction of new infrastructure, stadiums, and other facilities. Despite these challenges, the Olympics continue to capture the world's imagination, with athletes from all backgrounds and cultures coming together to compete at the highest level. 
            The Olympics remain a symbol of international cooperation, athletic excellence, and the power of sport to unite people from around the world.</p>""",unsafe_allow_html=True)
            st.markdown("<center><h1 class='ab-name'>The Modern Olympics Movement</h1>", unsafe_allow_html=True)
            st.markdown("""<p class='about'>The modern Olympics are held every four years, alternating between the summer and winter seasons. The Summer Olympics feature a wide range of sports, including athletics, swimming, gymnastics, basketball, volleyball, soccer, and many others. The Winter Olympics feature sports such as skiing, ice skating, bobsledding, and curling. The number of sports and athletes at the Olympics has increased significantly since the first modern Games. At the 1896 Olympics, there were just nine sports and 241 athletes from 14 countries. In contrast, the 2016 Summer Olympics in Rio de Janeiro featured 28 sports and over 11,000 athletes from 206 countries.
            In addition to the athletic competitions, the Olympics are also an important cultural event. The opening and closing ceremonies feature elaborate performances showcasing the host country's culture and history. The Olympics also provide an opportunity for athletes from around the world to interact and share their experiences, promoting understanding and goodwill among nations.
            </p>""", unsafe_allow_html=True)
            st.markdown("""<p class='about'>The International Olympic Committee (IOC) is responsible for overseeing the organization and management of the Olympic Games. The IOC is based in Lausanne, Switzerland and is composed of members from around the world. The IOC is responsible for selecting the host city for each Olympic Games, as well as establishing the rules and regulations for the Games.
            In addition to the Summer and Winter Olympics, there are also Youth Olympic Games and Special Olympics. The Youth Olympic Games were first held in Singapore in 2010 and are held every four years, alternating between the Summer and Winter Games. The Youth Olympics are open to athletes between the ages of 15 and 18 and feature a range of sports. The Special Olympics are for athletes with intellectual disabilities and are held every two years, alternating between Summer and Winter Games.
            </p>""", unsafe_allow_html=True)
            st.markdown("<center><h1 class='ab-name'>Why Olympics Data Analysis</h1>", unsafe_allow_html=True)
            st.markdown("""<p class='about'>An Olympics data analysis website is an important resource for sports fans, researchers, and anyone who is interested in the Olympic Games and their history. Such a website provides comprehensive data about the Olympic Games, including information about individual athletes, countries, and events. By making Olympic data accessible online, the website can help to increase the accessibility of the information. This means that anyone with an internet connection can access the data, regardless of their location or resources. Additionally, an Olympics data analysis website can help users to better understand the Games and the athletes who participate in them. By providing context and analysis, users can gain a deeper understanding of the events and their significance. </p>""",unsafe_allow_html=True)
            st.markdown("""<p class='about'>Furthermore, researchers can use the data provided by an Olympics data analysis website to conduct studies on topics such as athlete performance, country performance, and historical trends. This can help to advance the field of sports science and provide insights into the factors that contribute to success in athletics. Overall, an Olympics data analysis website can be a valuable and informative resource that enhances accessibility, understanding, and knowledge about the Games and facilitates research and analysis in the field of sports science.</p>""",unsafe_allow_html=True)
            st.markdown("""<p class='about'>Finally, an Olympics data analysis website can also be a valuable tool for researchers and journalists who want to study the Games and their impact. By providing comprehensive data that can be analyzed and studied, these websites can help to advance the field of sports science and provide new insights into the factors that contribute to success in athletics. For example, researchers might use the data to study how training methods have evolved over time, or to analyze the relationship between a country's economic development and its performance at the Games.
            Overall, an Olympics data analysis website can be a valuable and informative resource for anyone interested in the Olympic Games. By providing easy access to comprehensive data, contextual information, and analysis, these websites can enhance users' understanding of the Games and their history, and can facilitate research and analysis in the field of sports science.</p>""", unsafe_allow_html=True)

        if selected == "Summer Olympics":
            st.markdown("<center><h1 class='ab-name'>About Summer Olympics</h1>", unsafe_allow_html=True)
            st.markdown("""<p class='about'>The Summer Olympics is a global multi-sport event that takes place every four years, and it is widely regarded as one of the world's most prestigious athletic competitions. The modern Summer Olympics began in Athens, Greece, in 1896, and since then, it has grown to become one of the most popular sporting events in the world. The Games typically feature a wide range of sports, including athletics, swimming, gymnastics, cycling, volleyball, basketball, and many others.
            The Summer Olympics are governed by the International Olympic Committee (IOC), which oversees the planning and execution of the Games. The host city for each Olympics is selected several years in advance, and the planning process can take many years. The Olympics are a massive undertaking, involving thousands of athletes, coaches, officials, and volunteers from around the world.</p>""",unsafe_allow_html=True)
            st.markdown("""<p class='about'>One of the most notable features of the Summer Olympics is the Opening Ceremony, which marks the official start of the Games. The Opening Ceremony typically features a parade of athletes from each participating country, as well as cultural performances and the lighting of the Olympic flame. The Closing Ceremony marks the end of the Games and features a similar celebration of the athletes and their achievements.The Summer Olympics are a major international event that attracts millions of viewers from around the world. They are an opportunity for athletes to compete at the highest level of their sport, and for countries to come together and celebrate their shared love of sport and competition. Beyond the athletic competition, the Olympics also provide an opportunity for people from different cultures and backgrounds to come together and build connections and understanding. Overall, the Summer Olympics are a celebration of sport, culture, and international cooperation.</p>""", unsafe_allow_html=True)
            st.markdown("""<p class= 'about'>For more details<a href='https://summer-analysis-vo9q.onrender.com'> Click here</a></p>""",unsafe_allow_html=True)

        if selected == "Winter Olympics":
            st.markdown("<center><h1 class='ab-name'>About Winter Olympics</h1>", unsafe_allow_html=True)
            st.markdown("""<p class='about'>The Winter Olympics is a multi-sport event that takes place every four years, and it focuses on winter sports such as skiing, snowboarding, ice skating, and ice hockey. The first Winter Olympics were held in Chamonix, France, in 1924, and since then, the event has grown to become a major international sporting competition.
            Like the Summer Olympics, the Winter Olympics are governed by the International Olympic Committee (IOC) and involve athletes from around the world competing in a wide range of sports. The host city for each Winter Olympics is selected several years in advance, and the planning process can take many years. The Winter Olympics are a massive undertaking, involving thousands of athletes, coaches, officials, and volunteers from around the world.The Winter Olympics have a unique character and spirit that sets them apart from the Summer Olympics. The events often take place in mountainous areas, and the athletes are required to compete in cold, snowy, and sometimes challenging conditions. The Winter Olympics also showcase a different set of sports and events, such as cross-country skiing, ski jumping, and biathlon, that are not typically featured in the Summer Olympics.</p>""", unsafe_allow_html=True)
            st.markdown("""<p class= 'about'>For more details<a href='https://winter-analysiis.onrender.com'> Click here</a></p>""", unsafe_allow_html=True)

        if selected == "Overall Analysis":
            st.markdown("<center><h1 class='ab-name'>About Overall Analysis</h1>", unsafe_allow_html=True)
            st.markdown("""<p class='about'>The Summer and Winter Olympics are two major international multi-sport events that take place every four years. The Summer Olympics focus on sports such as athletics, swimming, gymnastics, cycling, and basketball, while the Winter Olympics focus on sports such as skiing, snowboarding, ice skating, and ice hockey. Both events are governed by the International Olympic Committee (IOC) and involve athletes from around the world competing at the highest level of their respective sports.The host city for each Olympics is selected several years in advance, and the planning process can take many years. </p>""",unsafe_allow_html=True)
            st.markdown("""<p class='about'>The Olympics are a massive undertaking, involving thousands of athletes, coaches, officials, and volunteers from around the world. Both events feature an Opening Ceremony that typically includes a parade of athletes from each participating country, as well as cultural performances and the lighting of the Olympic flame. The Closing Ceremony marks the end of the Games and features a similar celebration of the athletes and their achievements.
            The Summer and Winter Olympics are major international events that attract millions of viewers from around the world. They provide an opportunity for athletes to compete at the highest level of their sport, for countries to come together and celebrate their shared love of sport and competition, and for people from different cultures and backgrounds to build connections and understanding. Overall, the Summer and Winter Olympics are celebrations of sport, culture, and international cooperation that hold a special place in the hearts of sports enthusiasts around the world.</p>""",unsafe_allow_html=True)
            st.markdown("""<p class= 'about'>For more details<a href='https://overall-analysis-dclg.onrender.com'> Click here</a></p>""", unsafe_allow_html=True)

 # Bottom to top button
    st.markdown('''
                    <style>
                    button{
                    float: right;
                    margin-top: 50px;
                    margin-right: 70px;
                    font-size:25px !important;
                    color: #0099e6;
                    background-color: white;
                    border-color: #0099e6;
                    border-radius: 20%;
                    padding: 0px 7px 7px 7px;
                    }
                    </style>
                    ''', unsafe_allow_html=True)
    st.markdown(''' <a target="_self" href="#LinkToTop">
                            <button>
                                🔝
                            </button>
                        </a>''', unsafe_allow_html=True)
navigation_bar()
