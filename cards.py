import random

# does what it says on the tin
def shuffle_deck(deck) :
	random.shuffle(deck)

# pick card(s) - call this method multiple times to draw multiple unique cards from the deck
def get_cards(deck) :
	num = random.randint(0, len(deck))
	len_deck = len(deck)
	card = deck[num]
	del(deck[num]) # so we don't get the same card twice if we're calling this multipel times for the same hand
	rev = random.randint(-1,1) # is card reversed? zero (false) or 1 (true)
	drawn = (card, rev) # tuple of card dictionary + 1 or zero for reversal
	return drawn

# array of dicts for each card
def get_deck():
	deck= [
		{ "name" : "The Fool", "url" : "the_fool", "image" : "images/00.jpg", "desc" : "Immaturity, sincerity, the natural man, a free spirit. One who naturally knows his will and is worry free. A dreamer, careless and disinterested in practical matters. Travel." , "rdesc" : "Folly, failure, madness. Hindered travel." },
		{ "name" : "The Magician", "url" : "the_magician", "image" : "images/01.jpg" , "desc" : "Will, creativeness, adroitness, mastery, elasticity, autonomy, eloquence, craft, cunning. May imply a new beginning. The Magus is an autonomous person that knows where he is going and how to achieve its ends." , "rdesc" : "Indecision, weak will, ineptitude, dilettante. Deceitfulness, trickery." },
		{ "name" : "The High Priestess", "url" : "the_high_priestess", "image" : "images/02.jpg" , "desc" : "Hidden influence. Silence, patience, equilibrium. Slow but firm. Pondered decision. Advice, tuition, possibly given by a woman. Psychic ability. The manifestation of the eternal feminine in a spiritual way." , "rdesc" : "Deceptive, secret, or sly manner. Lazyness, intolerance. Delays. False ideas, moodiness, doubt, superficiality." },
		{ "name" : "The Empress", "url" : "the_empress", "image" : "images/03.jpg" , "desc" : "Understanding, charm, kindness, beauty, pleasure, success, safety, trust. Nurturing, positive development." , "rdesc" : "False appearance, vanity, disdain, frivolity. Sterility. Delays. Careless spending." },
		{ "name" : "The Emperor", "url" : "the_emperor", "image" : "images/04.jpg" , "desc" : "Stability. Power. Being in control of yourself/situation. Ambition. Leadership. Firmness of purpose. A dominant male person." , "rdesc" : "Loss of control. Emotional immaturity and bondage to parents. Possibility of being defrauded of one's inheritance. Ill-temper. Stubbornness. Fall. Loss of wealth. Megalomaniac." },
		{ "name" : "The Hierophant", "url" : "the_hierophant", "image" : "images/05.jpg" , "desc" : "Wisdom, endurance, persistence, patience, help from superiors, good advice, a good teacher, organization, peace, goodness of heart. The card that represents you, in the form of your own, truest voice, your own inner-self. Dogma. Can be lawyers." , "rdesc" : "Tendency to over criticize or being unduly concerned with the morals of others. Incapable of dealing efficiently with practical matters, especially finances. Unconventionality, illogical, superstitious, unable to behave coherently." },
		{ "name" : "The Lovers", "url" : "the_lovers", "image" : "images/06.jpg" , "desc" : "Union, decision, choice, marriage, love, the union of opposites, attraction. Balance, openness to inspiration. Harmony of the inner and outer aspect of life." , "rdesc" : "Disorder, failure, danger of a broken relationship or a wrong choice, quarrels, infidelity. Emotional instability. Dangerous temptation." },
		{ "name" : "The Chariot", "url" : "the_chariot", "image" : "images/07.jpg" , "desc" : "Triumph of the will, to surmount opposition, success. Self-control, ability to determinate the own destiny. Good news. Great physical and mental strength. Swiftness. The transitory power. Travel." , "rdesc" : "Generalized disorder. Illness. Dangerous restlessness. Danger of a violent accidente." },
		{ "name" : "Strength", "url" : "strength", "image" : "images/08.jpg" , "desc" : "Sublimation or regulation of the passions and lower instincts. Power, energy, great love. Spirit ruling over matter. Action, courage. Success. Powerful will and great physical strength. The inner strength to tame the lust." , "rdesc" : "Discord, ruin, stubbornness, abuse of power. Weakness." },
		{ "name" : "The Hermit", "url" : "the_hermit", "image" : "images/09.jpg" , "desc" : "Prudence, wisdom, patience, silence, spiritual advance, divine inspiration, circumspection, retirement from participation in current events, solitude. Pilgrimage. Quest for wisdom. Could be a teacher. A period of spiritual and intellectual personal development." , "rdesc" : "Immaturity, viciousness, darkness, stubbornness, deception, betrayal, too much or insufficient prudence. Misanthrope, misogyny, celibacy, excessively shy person. Hidden enemies." },
		{ "name" : "The Wheel of Fortune", "url" : "the_wheel_of_fortune", "image" : "images/10.jpg" , "desc" : "Change, evolution, success, good fortune, fate. Happiness, abundance. New conditions." , "rdesc" : "Retarded progress. Delays, setbacks." },
		{ "name" : "Justice", "url" : "justice", "image" : "images/11.jpg" , "desc" : "Conformity to moral rightness in action or attitude. The power to maintain equilibrium between the necessities and responsibilities of life. Justice, balance, adjustment. In order to keep things balanced certain things must be sacrificed.. May refer to law matters, trials, marriages, divorces, etc. Integrity, moderation." , "rdesc" : "Fanaticism, injustice, inequality, legal complications. Harsh judgment. Insecurity, imbalance." },
		{ "name" : "The Hanged Man", "url" : "the_hanged_man", "image" : "images/12.jpg" , "desc" : "Fortitude, wisdom. Self-imposed limitations. Voluntary sacrifice leading to new insight or initiation through tribulations and ordeals. Redemption through sacrifice, loss. Prophetic power. Suspended decisions. Choice requiring contemplation." , "rdesc" : "Arrogance, egotism, resistance to spiritual influences. Absorption in physical matters. Wasted effort. False prophecy. Failure." },
		{ "name" : "Death", "url" : "death", "image" : "images/13.jpg" , "desc" : "Complete transformation. Death and rebirth. The end of something. Evolution from one state to another." , "rdesc" : "Stagnation, death, petrification. Incurable ill person. Broken marriage." },
		{ "name" : "Temperance", "url" : "temperance", "image" : "images/14.jpg" , "desc" : "Careful consideration, patience, moderation, adaptation, tempering, self-control. To temper, to combine, to exercise self-restraint. Patience, bringing together two opposites carefully blending them. Good marriage. Working in harmony with others, good management. Something is brewing. Great talent and creative involvement. Striving for Transcendence through works. Alchemy. The union of opposites refined by the fire of the Will." , "rdesc" : "Disorder, conflict, unfortunate combinations, quarrels. Possibility of shipwreck." },
		{ "name" : "The Devil", "url" : "the_devil", "image" : "images/15.jpg" , "desc" : "Fate (wrong or good). Seductive power, blind impulse. Temptation, obsession. Sexual deviation. A disturbed mental state. Earthly passions are turning you inside and out." , "rdesc" : "Harmful, fate, wrong use of force, weakness, blindness, disorder. Malefic effects. The pathetic human condition of choosing illusion over truth." },
		{ "name" : "The Blasted Tower", "url" : "the_blasted_tower", "image" : "images/16.jpg" , "desc" : "Sudden changes without choice, collapse, escape from prison or bondages, accident. Plans will fall, intentions will break down. Finger of God. Bankruptcy. Sudden death." , "rdesc" : "Complete confusion. The gain of freedom at great cost. False accusations, oppression." },
		{ "name" : "The Star", "url" : "the_star", "image" : "images/17.jpg" , "desc" : "Hope, unexpected help, insight and clarity of vision, inspiration, flexibility. Great love will be given and received. Good health." , "rdesc" : "Arrogance, pessimism, stubbornness. Illness. Error of judgment." },
		{ "name" : "The Moon", "url" : "the_moon", "image" : "images/18.jpg" , "desc" : "Intuition, threshold of an important change, arduous and obscure path, development of psychic powers." , "rdesc" : "Unforeseen perils, secret foes, hallucination, self-deception, hysteria, disorientation. Blackmailer." },
		{ "name" : "The Sun", "url" : "the_sun", "image" : "images/19.jpg" , "desc" : "Glory. Material happiness. Happy marriage or relationship, collaboration. Success. Pleasure. Energy, motivation, inspiration to others." , "rdesc" : "Anoyances, disguise. Arrogance. Broken engagement or lost job." },
		{ "name" : "Judgement", "url" : "judgement", "image" : "images/20.jpg" , "desc" : "Radical change, resurrection to a new life. A work (or life) well done. Willingness to try something new. Good judgment and discernment. Creative power and influence over family and career. Forgiveness. Awakening. Legal judgments, in one's favor." , "rdesc" : "Spiritual vacillation, weakness, wrong judgment. Illness. Separation. Adverse legal judgment." },
		{ "name" : "The World", "url" : "the_world", "image" : "images/21.jpg" , "desc" : "Success granted. Rewards. Travel, emigration, change of residence." , "rdesc" : "Hindrances, stagnation. Hard work to bring success." },
		{ "name" : "King of Wands", "url" : "king_of_wands", "image" : "images/waki.jpg" , "desc" : "Courageous, swift and generous man. Passionate and strong. Paternalistic and proud. May be a country gentleman, generally married. Unexpected heritage; a good marriage." , "rdesc" : "Despotic, bigoted, prejudiced, evil-minded." },
		{ "name" : "Queen of Wands", "url" : "queen_of_wands", "image" : "images/waqu.jpg" , "desc" : "Kind, energetic but calm woman. Conservative, pragmatic and authoritarian. Fruitful in mind and body." , "rdesc" : "Domineering, jealous, dogmatic and irrational. Quick to take offense." },
		{ "name" : "Knight of Wands", "url" : "knight_of_wands", "image" : "images/wakn.jpg" , "desc" : "A young and energetic man. Swift and daring. May be noble and generous but also violent and hasty." , "rdesc" : "Jealous, weak and intolerant person. Quarrel, discord, frustration." },
		{ "name" : "Page of Wands", "url" : "page_of_wands", "image" : "images/wapa.jpg" , "desc" : "Young and brilliant. Enthusiastic and daring. A messenger or bearer of tidings." , "rdesc" : "Frivolous youth. Theatrical and shallow. Cruel, oppressive." },
		{ "name" : "Ace of Wands", "url" : "ace_of_wands", "image" : "images/wa01.jpg" , "desc" : "Creation, birth. The power or ability to begin or to follow through energetically with a plan or task; enterprise and determination. Beginning of an enterprise, invention or adventure." , "rdesc" : "Fall. To lose or postpone something (employment, enterprise, etc.). False starts." },
		{ "name" : "Two of Wands", "url" : "two_of_wands", "image" : "images/wa02.jpg" , "desc" : "Dominion. Maturity. Boldness with self-control. Influence." , "rdesc" : "Disturbance. Indifferent to or disregardful of consequences. Fear, illness." },
		{ "name" : "Three of Wands", "url" : "three_of_wands", "image" : "images/wa03.jpg" , "desc" : "Virtue. Established strength, realization of hope, nobility. Cooperation, partnership." , "rdesc" : "Inconsistency, deception, treachery. Loss, robbery." },
		{ "name" : "Four of Wands", "url" : "four_of_wands", "image" : "images/wa04.jpg" , "desc" : "Completion. Settlement, peace, harmony. Romance, marriage, society." , "rdesc" : "Insecurity. Uneasiness, unreliableness. Contradictions, incomplete happiness." },
		{ "name" : "Five of Wands", "url" : "five_of_wands", "image" : "images/wa05.jpg" , "desc" : "Strife. Competition, lawsuit, obstacles, violence, fighting." , "rdesc" : "Dangerous indecision, treachery, complication." },
		{ "name" : "Six of Wands", "url" : "six_of_wands", "image" : "images/wa06.jpg" , "desc" : "Victory after strife. Good news. Progress, helping friends." , "rdesc" : "Postponement. Insolence, excessive pride. Treason." },
		{ "name" : "Seven of Wands", "url" : "seven_of_wands", "image" : "images/wa07.jpg" , "desc" : "Valor. Victory through courage. Struggle. Fierce competition. Certain success." , "rdesc" : "Uncertainty and fear. Pregnancy. False appearance." },
		{ "name" : "Eight of Wands", "url" : "eight_of_wands", "image" : "images/wa08.jpg" , "desc" : "Swiftness. Hasty decision. Air travel, messages. Love letter. Hyperactivity. Great hopes." , "rdesc" : "Opposition. Jealousness. Delay in business or love affair." },
		{ "name" : "Nine of Wands", "url" : "nine_of_wands", "image" : "images/wa09.jpg" , "desc" : "Strength. Capability of enduring a long struggle and achieve the final victory. Recovery from sickness." , "rdesc" : "Weakness, delays, sickness. Adversity." },
		{ "name" : "Ten of Wands", "url" : "ten_of_wands", "image" : "images/wa10.jpg" , "desc" : "Oppression. Imbalance and selfishness. Heavy burden. Force detached from spiritual sources. A problem may be solved soon." , "rdesc" : "Annoyances. Treason. Separation, emigration. Some loses." },
		{ "name" : "King of Cups", "url" : "king_of_cups", "image" : "images/cuki.jpg" , "desc" : "A man skilled in law or trade and interested in science, art, religion or philosophy. A good friend, liberal, idealistic and creative. Kind and willing to take some responsibility." , "rdesc" : "A superficial man, easily enthusiastic, but with little depth of character. Untruthful, ruthless and vicious." },
		{ "name" : "Queen of Cups", "url" : "queen_of_cups", "image" : "images/cuqu.jpg" , "desc" : "Dreamy, calm, poetic, imaginative, kind yet not willing to take much trouble for another." , "rdesc" : "Dishonest and vicious woman, not to be trusted." },
		{ "name" : "Knight of Cups", "url" : "knight_of_cups", "image" : "images/cukn.jpg" , "desc" : "A young man may be an artist, who is graceful and poetic. He is an indolent dreamer of sensual pleasures. Can mean a messenger, a proposition or an invitation." , "rdesc" : "Lazy and deceitful. A dissolute and merciless person." },
		{ "name" : "Page of Cups", "url" : "page_of_cups", "image" : "images/cupa.jpg" , "desc" : "Quiet and studious youth, but also sweet and dreamy. News or proposition." , "rdesc" : "A sensual libertine, not harmful but neither helpful. Unpleasant news. Flatterer, selfish." },
		{ "name" : "Ace of Cups", "url" : "ace_of_cups", "image" : "images/cu01.jpg" , "desc" : "Harmony, fertility, happiness, beginning of great love." , "rdesc" : "Discord, false love, instability." },
		{ "name" : "Two of Cups", "url" : "two_of_cups", "image" : "images/cu02.jpg" , "desc" : "Love. Harmony, warm friendship. Close relation with a kindred soul. Good for business and love." , "rdesc" : "Opposition. False love. Folly, misunderstanding." },
		{ "name" : "Three of Cups", "url" : "three_of_cups", "image" : "images/cu03.jpg" , "desc" : "Abundance. Pleasure, hospitality, success. The good things of life." , "rdesc" : "Sensuality or food and drink intemperance." },
		{ "name" : "Four of Cups", "url" : "four_of_cups", "image" : "images/cu04.jpg" , "desc" : "Luxury. Abandonment to desire. New ambition." , "rdesc" : "Luxury that does not provide happiness. Dissatisfaction with material success. Turning point in life." },
		{ "name" : "Five of Cups", "url" : "five_of_cups", "image" : "images/cu05.jpg" , "desc" : "Disappointment. Unexpected misfortune. Partial loss. Friendship or love gone. Inheritance." , "rdesc" : "New happiness. Return of an old friend or love. Alliance." },
		{ "name" : "Six of Cups", "url" : "six_of_cups", "image" : "images/cu06.jpg" , "desc" : "Pleasure. Happiness coming from the past. Nostalgia. Success." , "rdesc" : "Uncertainty. Living too much in the past. Worthless associates. Inheritance." },
		{ "name" : "Seven of Cups", "url" : "seven_of_cups", "image" : "images/cu07.jpg" , "desc" : "Debauch. Foolish expectations. Illusory dreams, deceit. Intoxication. Drug addiction." , "rdesc" : "New will. Intelligent decision. Short travels." },
		{ "name" : "Eight of Cups", "url" : "eight_of_cups", "image" : "images/cu08.jpg" , "desc" : "Indolence. Instability. Material success abandoned, may be for something higher. Decline in interest. Wandering." , "rdesc" : "Joy, happiness. A new love or interest in material things.." },
		{ "name" : "Nine of Cups", "url" : "nine_of_cups", "image" : "images/cu09.jpg" , "desc" : "Happiness. Complete material success and well-being. You will get what you wish." , "rdesc" : "Imperfection, deceit. Intemperance. You will not get what you wish." },
		{ "name" : "Ten of Cups", "url" : "ten_of_cups", "image" : "images/cu10.jpg" , "desc" : "Satiety. Perfect love and lasting contentment. Peace, friendship." , "rdesc" : "Dissipation, loss of friendship. Betrayal. Waste." },
		{ "name" : "King of Swords", "url" : "king_of_swords", "image" : "images/swki.jpg" , "desc" : "This man may be a very good ally or counselor. He is clever and self-controlled and has some authority. Also is modern, analytical and very strong. The card may also mean a lawsuit." , "rdesc" : "Deceitful and malicious man. He may be a dangerous enemy, violent and powerful." },
		{ "name" : "Queen of Swords", "url" : "queen_of_swords", "image" : "images/swqu.jpg" , "desc" : "A graceful but stern woman. She has keen insight and good judgment. May be a dancer, a widow or a childless woman. This card also means privation and mourning." , "rdesc" : "Playfully mischievous. Dangerous enemy. Jealous and narrow-minded woman." },
		{ "name" : "Knight of Swords", "url" : "knight_of_swords", "image" : "images/swkn.jpg" , "desc" : "Audacious, clever and gallant; spirited young man. He may be domineering and unstable but he has the better intentions." , "rdesc" : "Harsh, fanatic, extravagant. Tyranic and aggressive. Dangerous enemy." },
		{ "name" : "Page of Swords", "url" : "page_of_swords", "image" : "images/swpa.jpg" , "desc" : "Logic and penetrating young man or woman. Mentally and physically dexterous. Spying. Messages." , "rdesc" : "Frivolous, revengeful and cunning. Indiscretion. Impotence. Unforeseen perturbation." },
		{ "name" : "Ace of Swords", "url" : "ace_of_swords", "image" : "images/sw01.jpg" , "desc" : "Conquest. Triumph through trouble. Intense activity. Gestation or parturition." , "rdesc" : "Disaster or conquest followed by disaster. Great loss. Violent death. Infertility." },
		{ "name" : "Two of Swords", "url" : "two_of_swords", "image" : "images/sw02.jpg" , "desc" : "Peace. Balanced forces. Indecision. Strength. Friendship." , "rdesc" : "Disloyalty. Change, sometimes in the wrong direction. Quarrel" },
		{ "name" : "Three of Swords", "url" : "three_of_swords", "image" : "images/sw03.jpg" , "desc" : "Sorrow. Separation, quarrel, tears. Delay. Absence." , "rdesc" : "Confusion, loss, error." },
		{ "name" : "Four of Swords", "url" : "four_of_swords", "image" : "images/sw04.jpg" , "desc" : "Truce. Solitude. Stagnation. Recovering from illness. Exile. Retreat." , "rdesc" : "Renewed activity. Surprise. Prudence and economy are advised." },
		{ "name" : "Five of Swords", "url" : "five_of_swords", "image" : "images/sw05.jpg" , "desc" : "Defeat. Failure. Loss. Powerlessness. Separation. Lies. Death." , "rdesc" : "Risk of loss or defeat. Funeral. Weakness." },
		{ "name" : "Six of Swords", "url" : "six_of_swords", "image" : "images/sw06.jpg" , "desc" : "Science. Journey by water, revelation, study. Intelligent effort. Success after anxiety." , "rdesc" : "Stagnation. Unfavorable result. Intellectual pride." },
		{ "name" : "Seven of Swords", "url" : "seven_of_swords", "image" : "images/sw07.jpg" , "desc" : "Futility. Partial or unpredictable result. Dreams, vacillation. Travel by land." , "rdesc" : "Quarrels. Slanders. Disenchantment in family or friendship." },
		{ "name" : "Eight of Swords", "url" : "eight_of_swords", "image" : "images/sw08.jpg" , "desc" : "Interference. Restriction. Temporal sickness or captivity. Indecision." , "rdesc" : "New beginnings. Freedom from the past bondages." },
		{ "name" : "Nine of Swords", "url" : "nine_of_swords", "image" : "images/sw09.jpg" , "desc" : "Cruelty. Suffering. Misery. Sickness. Martyrdom. Burden. May be death of a loved one." , "rdesc" : "Patience, faithfulness, unselfishness." },
		{ "name" : "Ten of Swords", "url" : "ten_of_swords", "image" : "images/sw10.jpg" , "desc" : "Ruin. Total defeat. Death. The end of an illusion." , "rdesc" : "Transitory success. Improvement." },
		{ "name" : "King of Pentacles", "url" : "king_of_pentacles", "image" : "images/peki.jpg" , "desc" : "A married man, wealthy and clever in money matters. Patient and laborious, he is an experimented chief and a reliable ally." , "rdesc" : "Vicious and greedy man. Beware or gamblers or speculators. Easy to bribe, he may be a dangerous man." },
		{ "name" : "Queen of Pentacles", "url" : "queen_of_pentacles", "image" : "images/pequ.jpg" , "desc" : "Charming and generous woman. Pragmatic and quiet, but ambitious. Opulence, security." , "rdesc" : "Foolish and temperamental. Prone to suspicion ad fearful of failure. Negligent." },
		{ "name" : "Knight of Pentacles", "url" : "knight_of_pentacles", "image" : "images/pekn.jpg" , "desc" : "Mature and responsible, a trustworthy and laborious man. A capable manager. An important matter concerning money." , "rdesc" : "Dull, lazy or clumsy man. Careless. Stagnation." },
		{ "name" : "Page of Pentacles", "url" : "page_of_pentacles", "image" : "images/pepa.jpg" , "desc" : "A learned young person, careful and reflective. Good management, kind and benevolent. The bearer of good news and messages." , "rdesc" : "Wasteful, illogical, rebellious youth. Bad news or lost of money." },
		{ "name" : "Ace of Pentacles", "url" : "ace_of_pentacles", "image" : "images/pe01.jpg" , "desc" : "The beginning of prosperity and wealth. Pleasure and beauty." , "rdesc" : "Success is delayed or it does not give happiness. Greed." },
		{ "name" : "Two of Pentacles", "url" : "two_of_pentacles", "image" : "images/pe02.jpg" , "desc" : "Change. Alternation of gain and loss. Equilibrium in the midst of change. Ability to adapt to new circumstances. Some complications. Unstable mood." , "rdesc" : "Uncertainty. Difficulty adapting to new circumstances." },
		{ "name" : "Three of Pentacles", "url" : "three_of_pentacles", "image" : "images/pe03.jpg" , "desc" : "Works. Task well done. Commercial transactions. Professional growth. Dignity. A male child." , "rdesc" : "Unsufficient skill or knowledge to achieve the goal. Fruitless work. Lack of seriousness." },
		{ "name" : "Four of Pentacles", "url" : "four_of_pentacles", "image" : "images/pe04.jpg" , "desc" : "Power. Purely material gain and security. A gift or an inheritance. A female child. Greed." , "rdesc" : "Prejudice. Limitation. Sudden check in progress or loss. Reckeless spending of money." },
		{ "name" : "Five of Pentacles", "url" : "five_of_pentacles", "image" : "images/pe05.jpg" , "desc" : "Worry. Loss of money or employment. Poverty. Defeat. Lovers. Sympathy found in the midst of trouble." , "rdesc" : "New employment or opportunity. Productive work. Misfortune in love." },
		{ "name" : "Six of Pentacles", "url" : "six_of_pentacles", "image" : "images/pe06.jpg" , "desc" : "Success. Material gain and power. Sharing with others the wealth." , "rdesc" : "Transitory gains. Prodigality. Bribery. Purse proud." },
		{ "name" : "Seven of Pentacles", "url" : "seven_of_pentacles", "image" : "images/pe07.jpg" , "desc" : "Failure. Defeat. Loss of money. Hard work but little gain. Greedy." , "rdesc" : "Delayed success after hard work. Work done for the love of work without expecting retribution." },
		{ "name" : "Eight of Pentacles", "url" : "eight_of_pentacles", "image" : "images/pe08.jpg" , "desc" : "Prudence. The first steps of a profitable profession. Learning a business or profession. Ability in material affairs. A brunette." , "rdesc" : "Greedy. Selfish in a petty way. Vanity." },
		{ "name" : "Nine of Pentacles", "url" : "nine_of_pentacles", "image" : "images/pe09.jpg" , "desc" : "Gain. Practical wisdom limited to everyday affairs and the home. Stability. Solitude. Inheritance." , "rdesc" : "Loss of friendship or a material thing. Cancelled project. Beware of knavery." },
		{ "name" : "Ten of Pentacles", "url" : "ten_of_pentacles", "image" : "images/pe10.jpg" , "desc" : "Wealth. Fulfillment of material fortune. Family matters. Inheritance. House." , "rdesc" : "Family misfortune. Loss of inheritance. Beware of risky projects." },
	]
	return deck

