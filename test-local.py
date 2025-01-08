from mira_sdk import MiraClient, CompoundFlow
from mira_sdk.exceptions import FlowError
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("API_KEY")

client = MiraClient(config={"API_KEY": api_key})     # Initialize Mira Client
flow = CompoundFlow(source="flow.yaml")      # Load flow configuration

sample_content = """Meme coins are a hot topic in the crypto space. However, people often overlook the story or narrative behind meme coins and still perceive them merely as “pictures” .
In reality, the true value and charm of meme coins lie not just in their imagery but in their inherent story and narrative.

Meme coins drive attention and participation through their names, images, and stories, transforming the investment paradigm into a gamified experience infused with fun and creativity.
Additionally, community engagement and collective identity strengthen the adoption and marketing of meme coins.
The power of storytelling is not merely an element of enjoyment but plays a crucial role in the crypto space by evoking emotional resonance, establishing a shared narrative framework, and paving new paths for promoting and popularizing digital assets.

Background and Origins of Meme Coins
Before examining the narrative characteristics of meme coins, it is essential to understand their background and origins. Meme coins are a type of cryptocurrency based on blockchain technology, placing greater emphasis on community participation and the spread of stories compared to traditional cryptocurrencies.

Meme coins originated in 2013 with Dogecoin, whose image is derived from the iconic “DOGE” meme circulating online. The story of Dogecoin holds significance beyond its imagery, carrying a deeper narrative.

What Are Meme Coins?
Meme coins are a type of cryptocurrency issued and traded on blockchain technology. Inspired by internet memes, images, and elements of popular culture, they are aptly named “meme coins.” Initially, their primary purpose was entertainment and social interaction, often lacking practical business applications. Meme coins are typically limited in supply and managed through smart contracts. These characteristics make them stand out and gain popularity within the crypto community.

The history of meme coins can be traced back to 2013, when a cryptocurrency themed around the dog meme, Dogecoin, gained attention. Since then, more meme coins such as Shiba Inu, People, PEPE, and BRC20 tokens have emerged. These meme coins generated significant buzz on social media, attracting numerous users and investors.

However, meme coins gained substantial attention in 2020 due to a specific event. The project “MEME” launched a game on the Ethereum blockchain that mimicked an auction system. Players could use meme coins to purchase virtual cards and trade them on secondary markets. The project’s originality and innovation caused meme coin prices to surge dramatically, drawing media coverage and heightened interest from investors.

Reasons for the Emergence of Meme Coins
Meme coins have risen as speculative assets, attracting a large number of investors. Their emergence can be attributed to several key factors:

The Rise of Social Media
With the growing popularity of social media, memes have rapidly spread across the internet. Meme coins, as digital assets, combine these cultural phenomena with blockchain technology, offering users new ways to interact and engage.
Community-Driven Innovation
Meme coins evolve through community-led innovation. In meme coin projects, developers and community members actively participate in design, marketing, and promotion, fostering a vibrant and creative community ecosystem.
Financialization Trend
The rise and trading activity of meme coins reflect the broader trend of financialization in the cryptocurrency market. Increasingly, investors are turning to the crypto market in search of high-risk, high-reward investment opportunities. Meme coins’ price volatility makes them attractive to speculators and traders seeking rapid gains in a short period.
The Core of Meme Coins: Establishing Value
Successful meme coins often evoke emotional resonance among people. The value represented by the token may encompass social issues and emotional needs. When individuals emotionally connect with a token, they are more likely to invest in or participate in it. Internet memes and cultural phenomena serve as the foundation for forming meme coin communities. Community members can actively participate in the development and promotion of the project, contributing through suggestions and feedback and engaging in the design, marketing, and promotion of the meme coin project.

This community-driven development model ensures that meme coin projects align with the needs of the community while enhancing participation and loyalty.

The specific roles performed by community members within the community include:

Creativity and Innovation
Community members are creative and innovative, constantly proposing new meme coin concepts and designs. Interaction and collaboration among community members drive the continuous growth and evolution of meme coin projects.
Knowledge Sharing and Education:
Community members exchange experiences, share knowledge, and provide educational and training resources. This knowledge-sharing fosters the growth and development of the meme coin community, helping new members better understand and participate in the projects.
Promotion and Advocacy:
Community members share their passion and beliefs through social media, forums, and other channels. This promotion by the community sparks interest within the cryptocurrency community and the broader internet audience, playing a vital role in the advancement and popularization of meme coins.
"""


test_input = {                                              # Prepare test inputs
    "content": sample_content,
    "content-type": "medium blog",
    "tone": "professional & authentic"
}                                         

try:
    response = client.flow.test(flow, test_input)           # Test entire pipeline
    print("Test response:", response)
except FlowError as e:
    print("Test failed:", str(e))    