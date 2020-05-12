import discord
from discord.ext import commands

class helper(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(
            color = discord.Colour.blue(),
            title = "Basic information of this bot",
            description = "Developer "
        )

    @commands.command(aliases=['h'])
    async def help(self, ctx, type=9):

        m = 'Sent you a DM!'

        embed = discord.Embed(
            color = discord.Color.blue(),
            title = "What would you like to know about coronavirus?",
            description = "Get information and guidance regarding the current outbreak of coronavirus disease (COVID-19) -\nSituation Report: https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports/ \nCoverage in Map: https://experience.arcgis.com/experience/685d0ace521648f8a5beeeee1b9125cd \n\n"
        )

        embed.add_field(name="Reply with the following commands to get the latest information of the topic -", value="``\n------------------------------------------------", inline=False)
        embed.add_field(name="`c!help 0` for", value="Bot commands\n------------------------------------------------", inline=False)
        embed.add_field(name="`c!help 1` for", value="how to protect yourself\n------------------------------------------------", inline=False)
        embed.add_field(name="`c!help 2` for", value="Your questions answered\n------------------------------------------------", inline=False)
        embed.add_field(name="`c!help 3` for", value="Mythbusters\n------------------------------------------------", inline=False)
        embed.add_field(name="`c!help 4` for", value="Travel Advice\n------------------------------------------------", inline=False)
        embed.add_field(name="`c!help 5` for", value="News & Press\n------------------------------------------------", inline=False)
        embed.add_field(name="Links -", value="Support Server = https://discord.com/invite/k9Vxdjd\nGitHub = https://github.com/HimanshuMS/covid-19_bot")

        embed0 = discord.Embed(
            color = discord.Color.blue(),
            title = "Statistics",
            description = "Statistics about spread of Coronavirus (COVID-19) around the world i.e Counting Numbers\n``\n------------------------------------------------"
        )

        embed0.add_field(name="c!stat` for", value="Total statistics of every countries combined\n------------------------------------------------", inline=False)
        embed0.add_field(name="`c!stat <country initials>` for", value="Checking statistics of a specific country, eg. `c!stat us` or `c!stat usa` or `c!stat uk` etc\n------------------------------------------------", inline=False)
        embed0.add_field(name="`c!stat <country name>` for", value="Checking statistics of a specific country, eg. `c!stat china` etc.\n------------------------------------------------", inline=False)
        embed0.add_field(name="`c!s <state>` and `c!s <state>, <district>` for", value="Checking statistics of specific state eg. `c!s Maharashtra`, and a district in that state eg. `c!s Maharashtra, Mumbai`\n------------------------------------------------", inline=False)
        embed0.add_field(name="`Fun Commands`", value="`c!tod <truth/dare>` truth and dare command\n------------------------------------------------", inline=False)
        embed0.set_footer(text="Inspired by picklejason ;)")

        embed1 = discord.Embed(
            color = discord.Color.dark_blue(),
            title = "How to protect yourself?",
            description = "Watch the video: https://youtu.be/8c_UJwLq8PI \n\n1. Wash your hands frequently for 15 to 20 seconds\n\n2. Avoid touching your eyes, mouth and nose\n\n3. Cover your mouth and nose with your elbow crease or tissue when you cough or sneeze\n\n4. Avoid crowded places or standing in group of 5 or more than 5 people\n\n5. Stay at home if you feel unwell - even with a slight fever and cough\n\n6. If you have a fever, cough and difficulty breathing, seek medical care early - seek help through call\n\n7. Stay updated of the latest information from WHO\n"
        )

        embed1.set_footer(text="for menu type c!help")

        embed2 = discord.Embed(
            color = discord.Color.blurple(),
            title = "Your questions answered",
            description = "\nReply with the number to get the correct answer -\n\n"
        )

        embed2.add_field(name="`c!help 20` command for", value="What are coronaviruses? What is COVID-19 and how is it related to SARS?", inline=False)
        embed2.add_field(name="`c!help 21` command for", value="What are the symptoms of COVID-19?", inline=False)
        embed2.add_field(name="`c!help 22` command for", value="How does COVID-19 spread?", inline=False)
        embed2.add_field(name="`c!help 23` command for", value="Can I catch COVID-19 from feces, animals or pets?", inline=False)
        embed2.add_field(name="`c!help 24` command for", value="Can I catch COVID-19 from infected surfaces of packages from infected areas?", inline=False)
        embed2.add_field(name="`c!help 25` command for", value="What can I do to protect myself and prevent the spread of virus?", inline=False)
        embed2.add_field(name="`c!help 26` command for", value="What should I do if I have visited an area where COVID-19 is spreading?", inline=False)
        embed2.add_field(name="`c!help 27` command for", value="What are the treatment options for COVID-19 (including drugs, vaccines, therapies?)", inline=False)
        embed2.add_field(name="`c!help 28` command for", value="Should I wear a mask to protect myself?", inline=False)
        embed2.add_field(name="`c!help 29` command for", value="Is there anything I should not do?", inline=False)
        embed2.add_field(name="`c!help 30` command for", value="How do I cope with stress during COVID-19?", inline=False)
        embed2.add_field(name="`c!help 31` command for", value="How do I help children to cope with stress during COVID-19?", inline=False)


        embed2.set_footer(text="for menu type c!help")

        embed3 = discord.Embed(
            color = discord.Color.dark_purple(),
            title = "WHO Mythbusters",
            description = "\nThere is a lot of misinformation circulating around. Following are the authentic facts -\n\nPeople of all ages CAN be infected by the coronavirus. Older people and people with pre-existing medical conditions (such as asthma, diabetes, heart diseases) appear to be more vulnerable to becoming severely ill with the virus.\n\nCold weather and snow CANNOT kill the coronavirus.\n\nThe coronavirus CAN be transmitted in areas with hot and humid climates.\n\nThe coronavirus CANNOT be transmitted through mosquito bites.\n\nThere is NO evidence that companion animals/pets such as dogs or cats transmit the coronavirus.\n\nTaking a hot bath DOES NOT prevent the coronavirus.\n\nUltraviolet light SHOULD NOT be used for sterilization and can cause skin irritation.\n\nThermal scanners CAN detect if people have a fever but CANNOT detect whether or not someone has the coronavirus.\n\nSpraying alcohol or chlorine all over your body WILL NOT kill viruses that have already entered your body.\n\nVaccines against pneumonia such as pneumococcal vaccine and Haemophilus Influenzae type b (Hib) vaccine, DO NOT provide protection against the coronavirus.\n\nThere is NO evidence that regularly rinsing the nose with saline has protected people from getting infected with the coronavirus.\v\vGarlic is healthy but there is NO evidence from the current outbreak that eating garlic has protected people from the coronavirus.\n\nAnibiotics DO NOT work aginst viruses, antibiotics only work against bacteria.\n\nTill date, there is NO specific medicine recommended to prevent or treat the coronavirus.\n\nCheck the facts on the WHO website: https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public/myth-busters\n"
        )

        embed3.set_footer(text="for menu type c!help")

        embed4 = discord.Embed(
            color = discord.Color.dark_magenta(),
            title = "Travel Advice",
            description = "\nWHO continues to advice to restrict/ban all travels and trades to the countries experiencing COVID-19.\n\nIt is highly recommended for travellers who are sick to cancel or avoid travelling to coronavirus affacted places, specifically olf aged travellers and people suffering from chronic diseases or facing poor health conditions. Affected places are those Countries, Territories or Cities experiencing ongoing outbreak of COVID-19.\n\nGeneral recommendations for all travellers include:\n\nWash your hands frequently for 15 to 20 seconds.\n\nAvoid touching your eyes, mouth and nose\n\nCover your mouth and nose with your elbow crease or tissue when you cough or sneeze.\n\nStay more than 2 meter(6 feet) away from a sick person\n\nFollow proper hygiene practices\n\nWear a mask and keep yourself in isolation if you are tested positive for COVID-19\n\n**Travellers returning from affected areas should - **\n\nAvoid going out and self isolate yourself for 14 days and follow your Country's quarantine protocol and take adviced preventive measures.\n\nIf you are having any one of the symptoms such as continuous fever, cough or having difficulty in breathing then contact local healthcares preferably by call, tell them about your travel history and get a COVID-19 test done as soon as possible.\n\nFor latest travel advice: https://www.who.int/emergencies/diseases/novel-coronavirus-2019/travel-advice \n\nFor the latest situation reports for affected areas: https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports/ \n\nFor advice on proper food hygiene practices: https://www.who.int/foodsafety/publications/consumer/en/5keys_en.pdf?ua=1&ua=1\n\nFor advice on visiting live animal markets: https://www.who.int/health-topics/coronavirus/who-recommendations-to-reduce-risk-of-transmission-of-emerging-pathogens-from-animals-to-humans-in-live-animal-markets"
        )

        embed4.set_footer(text="for menu type c!help")

        embed5 = discord.Embed(
            color = discord.Color.magenta(),
            title = "News & Press",
            description = "\n**Situation reports:** Situation reports provide the latest updates on the novel coronavirus outbreak/\n https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports/ \n\n**Rolling updates:** Rolling updates on coronavirus disease (COVID-19) sourced from across WHO media.\n https://who.int/emergencies/diseases/novel-coronavirus-2019/events-as-they-happen \n\n**News articles:** All news releases, statements and notes for the media.\n https://who.int/emergencies/diseases/novel-coronavirus-2019/media-resources/news \n\n**Press briefings:** Coronavirus disease (COVID-19) press briefings including videos, audio and transcripts.\nhttps://who.int/emergencies/diseases/novel-coronavirus-2019/media-resources/press-briefings"
        )

        embed5.set_footer(text="for menu type c!help")

        embed20 = discord.Embed(
            color = discord.Color.blurple(),
            title = "What are coronaviruses? What is COVID-19 and how are they related to SARS?",
            description = "\n**What is a coronavirus?**\nCoronaviruses are a large family of viruses which may cause illness in animals or humans. In humans, several coronaviruses are known to cause respirators infections ranging from the common cold to more severe diseases such as Middle Ease Respiratory Syndrome (MERS) and Severe Acute Respiratory Syndrome (SARS). The most recently discovered coronavirus causes coronavirus disease COVID-19\n\n**What is COVID-19?**\nCOVID-19 is the infectious disease caused by the most recently discovered coronavirus. This new virus and disease were unknown before the outbreak began in Wuhan, China, in December 2019.\n\n**Is COVID-19 same as SARS?**\nNo. The virus that causes COVID-19 and the one that caused the outbreak of Severe Acute Respiratory Syndrome (SARS) in 2003 are related to each other genetically, but the diseases they cause are quite different. SARS was more deadly but much less infectious than COVID-19. There have been no outbreaks of SARS anywhere in the world since 2003."
        )

        embed20.set_footer(text="`c!help 3` for questions and c!help for menu.")

        embed21 = discord.Embed(
            color = discord.Color.blurple(),
            title = "What are the symptoms of COVID-19?",
            description = "\n\nThe most common symptoms of COVID-19 are:\nFever\nTiredness\nDry cough\n\nSome patients may have aches and pains, nasal congestion, runny nose, sore throat or diarrhea.\n\nThese symptoms are usually mild and begin gradually. Some people become infected but don’t develop any symptoms and don't feel unwell.\n\nMost people (about 80%) recover from the disease without needing special treatment. Around 1 out of every 6 people who gets COVID-19 becomes seriously ill and develops difficulty breathing.\n\nOlder people, and those with underlying medical problems like high blood pressure, heart problems or diabetes, are more likely to develop serious illness.\n\n**People with fever, cough and difficulty breathing should seek medical attention.**"
        )

        embed21.set_footer(text="`c!help 3` for questions and c!help for menu.")

        embed22 = discord.Embed(
            color = discord.Color.blurple(),
            title = "How does COVID-19 spread?",
            description = "\n\nPeople can catch COVID-19 from others who have the virus.\n\nThe disease can spread from person to person through small droplets from the nose or mouth which are spread when a person with COVID-19 coughs or exhales.\n\nThese droplets land on objects and surfaces around the person.\n\nOther people then catch COVID-19 by touching these objects or surfaces, then touching their eyes, nose or mouth.\n\nPeople can also catch COVID-19 if they breathe in droplets from a person with COVID-19 who coughs out or exhales droplets. This is why it is important to stay more than 1 meter (3 feet) away from a person who is sick.\n\nWHO is assessing ongoing research on the ways COVID-19 is spread and will continue to share updated findings.\n\n**Can the virus that causes COVID-19 be transmitted through the air?**\nStudies to date suggest that the virus that causes COVID-19 is mainly transmitted through contact with respiratory droplets rather than through the air.\n\n**Can COVID-19 be caught from a person who has no symptoms?**\nThe main way the disease spreads is through respiratory droplets expelled by someone who is coughing. The risk of catching COVID-19 from someone with no symptoms at all is very low. However, many people with COVID-19 experience only mild symptoms. This is particularly true at the early stages of the disease. It is therefore possible to catch COVID-19 from someone who has, for example, just a mild cough and does not feel ill.\n\nWHO is assessing ongoing research on the period of transmission of COVID-19 and will continue to share updated findings."
        )

        embed22.set_footer(text="`c!help 3` for questions and c!help for menu.")

        embed23 = discord.Embed(
            color = discord.Color.blurple(),
            title = "Can I catch COVID-19 from feces, animals, pets, surfaces or packages?",
            description = "\n\n**Can I catch COVID-19 from the feces of someone with the disease?**\nThe risk of catching COVID-19 from the feces of an infected person appears to be low. While initial investigations suggest the virus may be present in feces in some cases, spread through this route is not a main feature of the outbreak. WHO is assessing ongoing research on the ways COVID-19 is spread and will continue to share new findings. Because this is a risk, however, it is another reason to clean hands regularly, after using the bathroom and before eating.\n\n**Can humans become infected with the COVID-19 from an animal source?**\nCoronaviruses are a large family of viruses that are common in animals. Occasionally, people get infected with these viruses which may then spread to other people. For example, SARS-CoV was associated with civet cats and MERS-CoV is transmitted by dromedary camels. Possible animal sources of COVID-19 have not yet been confirmed.\nTo protect yourself, such as when visiting live animal markets, avoid direct contact with animals and surfaces in contact with animals. Ensure good food safety practices at all times. Handle raw meat, milk or animal organs with care to avoid contamination of uncooked foods and avoid consuming raw or undercooked animal products.\n\n**Can I catch COVID-19 from my pet?**\nThere is no evidence that a dog, cat or any pet can transmit COVID-19. COVID-19 is mainly spread through droplets produced when an infected person coughs, sneezes or speaks. To protect yourself clean your hands frequently and thoroughly."
        )

        embed23.set_footer(text="`c!help 3` for questions and c!help for menu.")

        embed24 = discord.Embed(
            color = discord.Color.blurple(),
            title = "Can I catch COVID-19 from surfaces or packages?",
            description = "\n\n**How long does the virus survive on surfaces?**\nIt is not certain how long the virus that causes COVID-19 survives on surfaces, but it seems to behave like other coronaviruses. Studies suggest that coronaviruses (including preliminary information on the COVID-19 virus) may persist on surfaces for a few hours or up to several days. This may vary under different conditions (e.g. type of surface, temperature or humidity of the environment).\nIf you think a surface may be infected, clean it with simple disinfectant to kill the virus and protect yourself and others. Clean your hands with an alcohol-based hand rub or wash them with soap and water. Avoid touching your eyes, mouth, or nose.\n\n**Is it safe to receive a package from any area where COVID-19 has been reported?**\nYes. The likelihood of an infected person contaminating commercial goods is low and the risk of catching the virus that causes COVID-19 from a package that has been moved, travelled, and exposed to different conditions and temperature is also low."
        )
        
        embed24.set_footer(text="`c!help 3` for questions and c!help for menu.")

        embed25 = discord.Embed(
            color = discord.Color.blurple(),
            title = "What precautions I should take to prevent getting infected? Protection measures for everyone",
            description = "Stay aware of the latest information on the COVID-19 outbreak, available on the WHO website and through your national and local public health authority. Many countries around the world have seen cases of COVID-19 and several have seen outbreaks. Authorities in China and some other countries have succeeded in slowing or stopping their outbreaks. However, the situation is unpredictable so check regularly for the latest news.\n\nYou can reduce your chances of being infected or spreading COVID-19 by taking some simple precautions:\n\n**Regularly and thoroughly clean your hands with an alcohol-based hand rub or wash them with soap and water.**\nWhy? Washing your hands with soap and water or using alcohol-based hand rub kills viruses that may be on your hands.\n\n**Maintain at least 1 metre (3 feet) distance between yourself and anyone who is coughing or sneezing.**\nWhy?  When someone coughs or sneezes they spray small liquid droplets from their nose or mouth which may contain virus. If you are too close, you can breathe in the droplets, including the COVID-19 virus if the person coughing has the disease.\n\n**Avoid touching eyes, nose and mouth**\nWhy? Hands touch many surfaces and can pick up viruses. Once contaminated, hands can transfer the virus to your eyes, nose or mouth. From there, the virus can enter your body and can make you sick.\n\n** Make sure you, and the people around you, follow good respiratory hygiene. This means covering your mouth and nose with your elbow crease or tissue when you cough or sneeze. Then dispose of the used tissue immediately.**\n"
        )

        embed25.add_field(name="Why?", value="Droplets spread virus. By following good respiratory hygiene you protect the people around you from viruses such as cold, flu and COVID-19.\n\n", inline=False)
        embed25.add_field(name="Stay home if you feel unwell. If you have a fever, cough and difficulty breathing, seek medical attention and call in advance. Follow the directions of your local health authority.\nWhy?", value=" National and local authorities will have the most up to date information on the situation in your area. Calling in advance will allow your health care provider to quickly direct you to the right health facility. This will also protect you and help prevent spread of viruses and other infections.\n\n", inline=False)
        embed25.add_field(name="Keep up to date on the latest COVID-19 hotspots (cities or local areas where COVID-19 is spreading widely).", value="If possible, avoid traveling to places  – especially if you are an older person or have diabetes, heart or lung disease.**\n", inline=False)
        embed25.add_field(name="Why?", value="You have a higher chance of catching COVID-19 in one of these areas.", inline=False)
        embed25.set_footer(text="`c!help 3` for questions and c!help for menu.")

        embed26 = discord.Embed(
            color = discord.Color.blurple(),
            title = "What should I do if I have visited an area where COVID-19 is spreading?",
            description = "\n\nIf you have recently visited (past 14 days) areas where COVID-19 is spreading follow the guidance outlined in question 15. (What can I do to protect myself and prevent the spread of disease?) and do the following:\n\n**Self-isolate by staying at home if you begin to feel unwell, even with mild symptoms such as headache, low grade fever (37.3°C or above) and slight runny nose, until you recover.**\nIf it is essential for you to have someone bring you supplies or to go out, e.g. to buy food, then wear a mask to avoid infecting other people.\n\nWhy?\nAvoiding contact with others and visits to medical facilities will allow these facilities to operate more effectively and help protect you and others from possible COVID-19 and other viruses.\n\n**If you develop fever, cough and difficulty breathing, seek medical advice promptly as this may be due to a respiratory infection or other serious condition. Call in advance and tell your provider of any recent travel or contact with travelers.**\nWhy? Calling in advance will allow your health care provider to quickly direct you to the right health facility. This will also help to prevent possible spread of COVID-19 and other viruses."
        )

        embed26.set_footer(text="`c!help 3` for questions and c!help for menu.")

        embed27 = discord.Embed(
            color = discord.Color.blurple(),
            title = "What are the treatment options for COVID-19 (including drugs, vaccines, therapies)?",
            description = "\n\n**Are antibiotics effective in preventing or treating COVID-19?**\nNo. Antibiotics do not work against viruses, they only work on bacterial infections. COVID-19 is caused by a virus, so antibiotics do not work. Antibiotics should not be used as a means of prevention or treatment of COVID-19. They should only be used as directed by a physician to treat a bacterial infection.\n\n**Are there any medicines or therapies that can prevent or cure COVID-19?**\nWhile some western, traditional or home remedies may provide comfort and alleviate symptoms of COVID-19, there is no evidence that current medicine can prevent or cure the disease. WHO does not recommend self-medication with any medicines, including antibiotics, as a prevention or cure for COVID-19. However, there are several ongoing clinical trials that include both western and traditional medicines. WHO will continue to provide updated information as soon as clinical findings are available.\n\n**Is there a vaccine, drug or treatment for COVID-19?**\nNot yet. To date, there is no vaccine and no specific antiviral medicine to prevent or treat COVID-2019. However, those affected should receive care to relieve symptoms. People with serious illness should be hospitalized. Most patients recover thanks to supportive care.\nPossible vaccines and some specific drug treatments are under investigation. They are being tested through clinical trials. WHO is coordinating efforts to develop vaccines and medicines to prevent and treat COVID-19.\nThe most effective ways to protect yourself and others against COVID-19 are to frequently clean your hands, cover your cough with the bend of elbow or tissue, and maintain a distance of at least 1 meter (3 feet) from people who are coughing or sneezing."
        )

        embed27.set_footer(text="`c!help 3` for questions and c!help for menu.")

        embed28 = discord.Embed(
            color = discord.Color.blurple(),
            title = "Should I wear a mask to protect myself?",
            description = "\n\nOnly wear a mask if you are ill with COVID-19 symptoms (especially coughing) or looking after someone who may have COVID-19. Disposable face mask can only be used once. If you are not ill or looking after someone who is ill then you are wasting a mask. There is a world-wide shortage of masks, so WHO urges people to use masks wisely.\n\nWHO advises rational use of medical masks to avoid unnecessary wastage of precious resources and mis-use of masks.\n\nThe most effective ways to protect yourself and others against COVID-19 are to frequently clean your hands, cover your cough with the bend of elbow or tissue and maintain a distance of at least 1 meter (3 feet) from people who are coughing or sneezing.\n\n**How to put on, use, take off and dispose of a mask?**\n1. Remember, a mask should only be used by health workers, care takers, and individuals with respiratory symptoms, such as fever and cough.\n2. Before touching the mask, clean hands with an alcohol-based hand rub or soap and water\n3. Take the mask and inspect it for tears or holes.\n4. Orient which side is the top side (where the metal strip is).\n5. Ensure the proper side of the mask faces outwards (the coloured side).\n6. Place the mask to your face. Pinch the metal strip or stiff edge of the mask so it moulds to the shape of your nose.\n7. Pull down the mask’s bottom so it covers your mouth and your chin.\n8. After use, take off the mask; remove the elastic loops from behind the ears while keeping the mask away from your face and clothes, to avoid touching potentially contaminated surfaces of the mask.\n9. Discard the mask in a closed bin immediately after use.\n10. Perform hand hygiene after touching or discarding the mask – Use alcohol-based hand rub or, if visibly soiled, wash your hands with soap and water."
        )

        embed28.set_footer(text="`c!help 3` for questions and c!help for menu.")

        embed29 = discord.Embed(
            color = discord.Color.blurple(),
            title = "Is there anything I should abnegate?",
            description = "\n\nThe following measures ARE NOT effective against COVID-19 and can be harmful:\n\nSmoking\nWearing multiple masks\nTaking antibiotics\n\nIn any case, if you have fever, cough and difficulty breathing seek medical care early to reduce the risk of developing a more severe infection and be sure to share your recent travel history with your health care provider."
        )

        embed29.set_footer(text="`c!help 3` for questions and c!help for menu.")

        embed30 = discord.Embed(
            color = discord.Color.blurple(),
            title = "Coping with stress during COVID-19",
            description = "\n\nIt is normal to feel sad, stressed, confused, scared or angry during a crisis. Talking to people you trust can help. Contact your friends and family.\n\nIf you must stay at home, maintain a healthy lifestyle - including proper diet, sleep, exercise and social contacts with loved ones at home and by email and phone with other family and friends.\n\nDon’t use smoking, alcohol or other drugs to deal with your emotions. If you feel overwhelmed, talk to a health worker or counsellor. Have a plan, where to go to and how to seek help for physical and mental health needs if required.\n\nGet the facts. Gather information that will help you accurately determine your risk so that you can take reasonable precautions. Find a credible source you can trust such as WHO website or, a local or state public health agency.\n\nLimit worry and agitation by lessening the time you and your family spend watching or listening to media coverage that you perceive as upsetting.\n\nDraw on skills you have used in the past that have helped you to manage previous life’s adversities and use those skills to help you manage your emotions during the challenging time of this outbreak."
        )

        embed30.set_footer(text="`c!help 3` for questions and c!help for menu.")

        embed31 = discord.Embed(
            color = discord.Color.blurple(),
            title = "Helping children cope with stress during COVID-19",
            description = "\n\nChildren may respond to stress in different ways such as being more clingy, anxious, withdrawing, angry or agitated, bedwetting etc. Respond to your child’s reactions in a supportive way, listen to their concerns and give them extra love and attention.\n\nChildren need adults’ love and attention during difficult times. Give them extra time and attention. Remember to listen to your children, speak kindly and reassure them. If possible, make opportunities for the child to play and relax.\n\nTry and keep children close to their parents and family and avoid separating children and their caregivers to the extent possible. If separation occurs (e.g. hospitalization) ensure regular contact (e.g. via phone) and re-assurance\n\nKeep to regular routines and schedules as much as possible, or help create new ones in a new environment, including school/learning as well as time for safely playing and relaxing.\n\nProvide facts about what has happened, explain what is going on now and give them clear information about how to reduce their risk of being infected by the disease in words that they can understand depending on their age. This also includes providing information about what could happen in a re-assuring way (e.g. a family member and/or the child may start not feeling well and may have to go to the hospital for some time so doctors can help them feel better)."
        )

        embed31.set_footer(text="`c!help 3` for questions and c!help for menu.")

        server = ctx.guild

        if(type==0):
            await ctx.author.send(embed=embed0)
            if (len(server.members) > 0):
                await ctx.send(m)
        elif(type==9):
            await ctx.author.send(embed=embed)
            if (len(server.members) > 0):
                await ctx.send(m)
        elif(type==1):
            await ctx.author.send(embed=embed1)
            if (len(server.members) > 0):
                await ctx.send(m)
        elif(type==2):
            await ctx.author.send(embed=embed2)
            if (len(server.members) > 0):
                await ctx.send(m)
        elif(type==3):
            await ctx.author.send(embed=embed3)
            if (len(server.members) > 0):
                await ctx.send(m)
        elif(type==4):
            await ctx.author.send(embed=embed4)
            if (len(server.members) > 0):
                await ctx.send(m)
        elif(type==5):
            await ctx.author.send(embed=embed5)
            if (len(server.members) > 0):
                await ctx.send(m)
        elif(type==20):
            await ctx.author.send(embed=embed20)
            if (len(server.members) > 0):
                await ctx.send(m)
        elif(type==21):
            await ctx.author.send(embed=embed21)
            if (len(server.members) > 0):
                await ctx.send(m)
        elif(type==22):
            await ctx.author.send(embed=embed22)
            if (len(server.members) > 0):
                await ctx.send(m)
        elif(type==23):
            await ctx.author.send(embed=embed23)
            if (len(server.members) > 0):
                await ctx.send(m)
        elif(type==24):
            await ctx.author.send(embed=embed24)
            if (len(server.members) > 0):
                await ctx.send(m)
        elif(type==25):
            await ctx.author.send(embed=embed25)
            if (len(server.members) > 0):
                await ctx.send(m)
        elif(type==26):
            await ctx.author.send(embed=embed26)
            if (len(server.members) > 0):
                await ctx.send(m)
        elif(type==27):
            await ctx.author.send(embed=embed27)
            if (len(server.members) > 0):
                await ctx.send(m)
        elif(type==28):
            await ctx.author.send(embed=embed28)
            if (len(server.members) > 0):
                await ctx.send(m)
        elif(type==29):
            await ctx.author.send(embed=embed29)
            if (len(server.members) > 0):
                await ctx.send(m)
        elif(type==30):
            await ctx.author.send(embed=embed30)
            if (len(server.members) > 0):
                await ctx.send(m)
        elif(type==31):
            await ctx.author.send(embed=embed31)
            if (len(server.members) > 0):
                await ctx.send(m)
        else:
            await ctx.author.send(embed=embed)
            if (len(server.members) > 0):
                await ctx.send(m)

def setup(bot):
    bot.add_cog(helper(bot))