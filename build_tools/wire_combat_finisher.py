# -*- coding: utf-8 -*-
"""
Script to wire the Conditional V3 Mortal Kombat Finisher & Ducking into playPlayerCombatAnimation.
"""
import sys

def main():
    path = "web/index.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Locate playPlayerCombatAnimation
    target_start = "function playPlayerCombatAnimation({"
    if target_start not in content:
        print("Error: playPlayerCombatAnimation not found")
        sys.exit(1)

    # Let's inspect the exact lines to replace
    # We want to replace from function playPlayerCombatAnimation({ ... to the end of the function.
    
    # Let's find function start and end
    start_idx = content.find(target_start)
    # The function ends right before "function pendingAIFixtureCount(){"
    end_marker = "function pendingAIFixtureCount(){"
    end_idx = content.find(end_marker, start_idx)
    if end_idx == -1:
        print("Error: end_marker not found")
        sys.exit(1)

    old_fn = content[start_idx:end_idx]

    new_fn = """function playPlayerCombatAnimation({containerId,leftMonster,rightMonster,leftRating,rightRating,leftWins,resultHtml,onComplete,opponentIsOwned=false,combatLabel='',rightMonsterForceTierArt=false,rightMonsterForcedTierIndex=null,leftFighterTag='YOUR MONSTER',rightFighterTag='OPPONENT AI',replayNote='Visual replay only · The existing combat result, rewards and league progression are unchanged'}){
 // Scope every animated element to this bout's container: league/championship logs may retain old scenes, so global ID lookups can animate the wrong fight.
 const container=document.getElementById(containerId);
 const legendFightButton=document.getElementById('legendFightBtn');
 if(!container){combatAnimationBusy=false;if(onComplete)onComplete();return;}
 combatAnimationBusy=true;

 // Duck background music during active combat
 if (typeof bgmManager !== 'undefined' && bgmManager.duck) bgmManager.duck();

 const names=[leftMonster?.name||'Your monster',rightMonster?.name||'Opponent'];
 const isOmegaSovereign=!!rightMonster?.isOmegaSovereign;
 const ratings=[Math.round(Number(leftRating)||combatRatingForVisual(leftMonster)),Math.round(Number(rightRating)||combatRatingForVisual(rightMonster))];
 const ratio=Math.min(Math.max(1,ratings[0]),Math.max(1,ratings[1]))/Math.max(1,ratings[0],ratings[1]);
 const winnerIndex=leftWins?0:1, loserIndex=winnerIndex===0?1:0;
 const winnerName=names[winnerIndex],loserName=names[loserIndex];

 // Check conditional V3 MK Finisher: Common Dire Wolf defeats Common War Rhino
 const isWolfVsRhinoFinisher = 
   speciesKeyForMonster(leftMonster) === 'wolf' &&
   rarityLabel(leftMonster) === 'Common' &&
   speciesKeyForMonster(rightMonster) === 'rhino' &&
   rarityLabel(rightMonster) === 'Common' &&
   leftWins === true;

 // These health bars and damage figures are theatrical only: real combat results/rewards have already been resolved.
 const winnerHit=Math.round(7+ratio*9);
 const loserHit=Math.round(18+(1-ratio)*24);
 const artLeft=safeCombatPortraitArt(leftMonster),artRight=safeCombatPortraitArt(rightMonster,rightMonsterForceTierArt,rightMonsterForcedTierIndex);
 container.classList.add('player-combat-log');
 container.innerHTML=`<div class="player-combat-scene" id="playerCombatScene" style="position:relative;">
   <div class="combat-scene-header"><div class="combat-live-tag"><span class="combat-live-dot"></span> ${combatLabel||(containerId==='champLog'?'Championship bout · Live fight animation':'League bout · Live fight animation')}</div><div class="combat-round-tools"><div class="combat-round-tag" id="combatRoundTag">EXCHANGE 1 / 3</div><button class="combat-sfx-toggle" id="combatSfxToggle" type="button" aria-pressed="false" title="Toggle optional fight sound effects">🔇 SFX OFF</button></div></div>
   <div class="combat-visual-arena">
    <article class="combat-fighter side-player ${leftWins?'fighter-winner':'fighter-loser'}" id="combatLeftFighter">
     <div class="combat-identity"><div style="min-width:0"><span class="combat-fighter-tag">${esc(leftFighterTag)}</span><div class="combat-fighter-name">${esc(names[0])}</div></div></div>
     <div class="combat-health-meta"><span id="combatLeftHealthText">100%</span></div><div class="combat-health-track"><span class="combat-health-fill" id="combatLeftHealth" style="width:100%"></span></div>
     <div class="combat-portrait">${artLeft}<div class="combat-hit-pop" id="combatLeftHit"></div></div>
    </article>
    <div class="combat-mid"><div class="combat-vs-mark"><span>VS</span></div><div class="combat-impact" id="combatImpact"></div></div>
    <article class="combat-fighter side-opponent ${leftWins?'fighter-loser':'fighter-winner'} ${isOmegaSovereign?'omega-sovereign-fighter':''}" id="combatRightFighter">
     <div class="combat-identity"><div style="min-width:0"><span class="combat-fighter-tag">${esc(rightFighterTag)}</span><div class="combat-fighter-name">${esc(names[1])}</div></div></div>
     <div class="combat-health-meta"><span id="combatRightHealthText">100%</span></div><div class="combat-health-track"><span class="combat-health-fill" id="combatRightHealth" style="width:100%"></span></div>
     <div class="combat-portrait">${artRight}<div class="combat-hit-pop" id="combatRightHit"></div></div>
    </article>
    <div class="combat-knockout-banner" id="combatKnockoutBanner" aria-hidden="true">K.O.</div>
   </div>
   <div class="combat-action-panel" aria-live="polite"><div class="combat-action-copy"><div class="combat-action-title" id="combatActionTitle">FIRST CLASH</div><div class="combat-action-text" id="combatActionText">Both monsters charge into the arena.</div></div><div class="combat-segment-indicator" aria-label="Combat exchange progress"><span class="active"></span><span></span><span></span></div></div>
   <div class="combat-replay-note">${esc(replayNote)}</div>
   <div class="combat-result-output" id="combatResultOutput"></div>
  </div>`;
 const scene=container.querySelector('.player-combat-scene');
 if(!scene){
  console.error('Combat replay could not find the scene inserted into its target log.');
  combatAnimationBusy=false;
  if (typeof bgmManager !== 'undefined' && bgmManager.restore) bgmManager.restore();
  if(typeof onComplete==='function')onComplete();
  return;
 }
 // Bring live league and Legends bouts into view as soon as their replay starts.
 if(containerId==='leagueLog'||containerId==='legendFightLog'||containerId==='cupFightLog'){
  scene.style.scrollMarginTop='14px';
  window.setTimeout(()=>{if(scene.isConnected)scene.scrollIntoView({behavior:'smooth',block:'start',inline:'nearest'});},40);
 }
 const fillLeft=scene.querySelector('#combatLeftHealth'),fillRight=scene.querySelector('#combatRightHealth');
 const textLeft=scene.querySelector('#combatLeftHealthText'),textRight=scene.querySelector('#combatRightHealthText');
 const hitLeft=scene.querySelector('#combatLeftHit'),hitRight=scene.querySelector('#combatRightHit');
 const roundTag=scene.querySelector('#combatRoundTag'),actionTitle=scene.querySelector('#combatActionTitle'),actionText=scene.querySelector('#combatActionText');
 const knockoutBanner=scene.querySelector('#combatKnockoutBanner');
 const sfxToggle=scene.querySelector('#combatSfxToggle');
 const syncSfxToggle=()=>{sfxToggle.textContent=combatSfxEnabled?'🔊 SFX ON':'🔇 SFX OFF';sfxToggle.setAttribute('aria-pressed',String(combatSfxEnabled));sfxToggle.setAttribute('aria-label',combatSfxEnabled?'Turn fight sound effects off':'Turn fight sound effects on');};
 sfxToggle.addEventListener('click',event=>{event.stopPropagation();combatSfxEnabled=!combatSfxEnabled;syncSfxToggle();if(combatSfxEnabled)primeCombatSfx();});
 syncSfxToggle();
 const indicator=[...scene.querySelectorAll('.combat-segment-indicator span')];
 const leftFighter=scene.querySelector('#combatLeftFighter'),rightFighter=scene.querySelector('#combatRightFighter');
 const leftWon=!!leftWins;
 let hpLeft=100,hpRight=100,step=0,replayFinished=false;
 const delays=[1250,1480,1700];
 const phaseTitles=isWolfVsRhinoFinisher ? [
   'FIRST CLASH',
   'TURNING POINT',
   'FINISHING BLOW — HELLFANG SPINE-BREAKER'
 ] : ['FIRST CLASH','TURNING POINT','FINISHING BLOW'];
 const phaseCopy=isWolfVsRhinoFinisher ? [
   `War Rhino charges forward with brute force! ${names[0]} takes the brunt of the opening impact.`,
   `${names[0]} roars back! Claws slash into the armoured hide, staggering the War Rhino!`,
   `Ravager bloodline awakening! ${names[0]} unleashes the Hellfang Spine-Breaker fatality!`
 ] : [
   `Both monsters surge forward and trade opening blows.`,
   `${winnerName} finds an opening and lands a crushing strike. ${loserName} manages a weaker counter.`,
   `${winnerName} commits to one decisive attack. ${loserName} is knocked out!`
 ];
 const setHealth=(side,value,damage,stage)=>{
   const hp=Math.max(0,Math.min(100,Math.round(value)));
   const fill=side==='left'?fillLeft:fillRight;
   const text=side==='left'?textLeft:textRight;
   const hit=side==='left'?hitLeft:hitRight;
   if(side==='left')hpLeft=hp;else hpRight=hp;
   fill.style.width=hp+'%';text.textContent=hp+'%';
   fill.classList.toggle('warning',hp<=60&&hp>30);fill.classList.toggle('low',hp<=30);
   hit.classList.remove('show','knockout-pop');void hit.offsetWidth;
   if(stage===3&&hp===0){hit.textContent='';return;}
   hit.textContent=`−${Math.max(0,Math.round(damage))}%`;
   hit.classList.add('show');
 };

 const finishCombatBout=()=>{
   if(replayFinished)return;
   try{
     const output=scene.querySelector('#combatResultOutput');
     if(output){output.innerHTML=resultHtml||'';output.classList.add('show');}
     const a=document.getElementById('leagueBoutBtn'),b=document.getElementById('champFightBtn'),c=document.getElementById('cupFightButton');
     if(a)a.disabled=false;if(b)b.disabled=false;if(c)c.disabled=false;
     combatAnimationBusy=false;replayFinished=true;
     if (typeof bgmManager !== 'undefined' && bgmManager.restore) bgmManager.restore();
     if(legendFightButton){const legendASelect=document.getElementById('legendA'),legendBSelect=document.getElementById('legendB');legendFightButton.disabled=!legendASelect||!legendBSelect||!legendASelect.value||!legendBSelect.value||legendASelect.value===legendBSelect.value;}
     if(typeof onComplete==='function'){const callback=onComplete;onComplete=null;callback();}
   }catch(error){recoverCombatReplay(error);}
 };

 const playVideoFinisher=()=>{
   const overlay=document.createElement('div');
   overlay.className='combat-finisher-overlay';
   overlay.style.cssText='position:absolute;inset:0;z-index:60;background:#000;display:flex;align-items:center;justify-content:center;border-radius:14px;overflow:hidden;box-shadow:0 8px 32px rgba(0,0,0,0.8);';
   overlay.innerHTML=`<video id="combatFinisherVideo" src="assets/video/Monster_Stud_Battle_Scene_01-v3_20261107223758.mp4" playsinline style="width:100%;height:100%;object-fit:cover;"></video>
   <button type="button" id="skipFinisherBtn" class="btn secondary" style="position:absolute;top:12px;right:12px;z-index:70;font-size:12px;padding:6px 14px;background:rgba(20,25,38,0.85);backdrop-filter:blur(8px);border:1px solid #48546a;color:#fff;">Skip Finisher ⏭</button>`;
   scene.appendChild(overlay);

   const v=overlay.querySelector('#combatFinisherVideo');
   const skipBtn=overlay.querySelector('#skipFinisherBtn');
   let finisherDone=false;

   const closeOverlay=()=>{
     if(finisherDone)return;
     finisherDone=true;
     v.pause();
     if(overlay.isConnected)overlay.remove();
     setHealth('right',0,hpRight,3);
     rightFighter.classList.add('fighter-knocked-out');
     knockoutBanner.classList.remove('show');void knockoutBanner.offsetWidth;knockoutBanner.classList.add('show');
     playCombatSfx('knockout');
     window.setTimeout(finishCombatBout,1100);
   };

   skipBtn.addEventListener('click',e=>{e.stopPropagation();closeOverlay();});
   v.addEventListener('ended',closeOverlay,{once:true});
   v.addEventListener('error',closeOverlay,{once:true});

   try{
     v.currentTime=18.0;
     v.muted=false;
     const playPromise=v.play();
     if(playPromise&&typeof playPromise.catch==='function'){
       playPromise.catch(()=>{
         v.muted=true;
         v.play().catch(closeOverlay);
       });
     }
   }catch(err){
     closeOverlay();
   }
 };

 const applyStageDamage=()=>{
   if(replayFinished||!scene.isConnected)return;
   playCombatSfx(step===3?'knockout':'impact');
   const prevLeft=hpLeft,prevRight=hpRight;
   if(step<3){
     if(isWolfVsRhinoFinisher){
       // Exchange 1: War Rhino wins opening exchange (Wolf takes heavier hit)
       // Exchange 2: Dire Wolf retaliates (Rhino takes heavier hit)
       if(step===1){
         setHealth('left',hpLeft-loserHit,Math.min(prevLeft,loserHit),step);
         setHealth('right',hpRight-winnerHit,Math.min(prevRight,winnerHit),step);
       }else{
         setHealth('left',hpLeft-winnerHit,Math.min(prevLeft,winnerHit),step);
         setHealth('right',hpRight-loserHit,Math.min(prevRight,loserHit),step);
       }
     }else{
       const playerTakes=leftWon?winnerHit:loserHit;
       const opponentTakes=leftWon?loserHit:winnerHit;
       setHealth('left',hpLeft-playerTakes,Math.min(prevLeft,playerTakes),step);
       setHealth('right',hpRight-opponentTakes,Math.min(prevRight,opponentTakes),step);
     }
   }else{
     if(isWolfVsRhinoFinisher){
       playVideoFinisher();
       return;
     }
     const winnerCounterHit=Math.max(3,Math.round(winnerHit*.45));
     if(leftWon){setHealth('left',hpLeft-winnerCounterHit,Math.min(prevLeft,winnerCounterHit),step);setHealth('right',0,prevRight,step);rightFighter.classList.add('fighter-knocked-out');}
     else{setHealth('right',hpRight-winnerCounterHit,Math.min(prevRight,winnerCounterHit),step);setHealth('left',0,prevLeft,step);leftFighter.classList.add('fighter-knocked-out');}
     knockoutBanner.classList.remove('show');void knockoutBanner.offsetWidth;knockoutBanner.classList.add('show');
   }
 };

 const updateStage=()=>{
   if(replayFinished||!scene.isConnected)return;
   step++;
   scene.classList.remove('stage-1','stage-2','stage-3','impact-flash');void scene.offsetWidth;
   scene.classList.add(`stage-${step}`,'impact-flash');
   roundTag.textContent=`EXCHANGE ${step} / 3`;
   actionTitle.textContent=phaseTitles[step-1];actionText.textContent=phaseCopy[step-1];
   indicator.forEach((dot,i)=>dot.classList.toggle('active',i<step));
   // Keep SFX synced to impact instead of the wind-up; impact/KO sounds play inside applyStageDamage.
   // Trigger health loss and damage text as the attack connects, not when the wind-up starts.
   window.setTimeout(()=>{try{applyStageDamage();}catch(error){recoverCombatReplay(error);}},225);
   window.setTimeout(()=>{scene.classList.remove('impact-flash');},650);
   if(step<3){
     window.setTimeout(safeUpdateStage,delays[step-1]);
   }else if(!isWolfVsRhinoFinisher){
     // Standard 2D knockout finish delay
     window.setTimeout(finishCombatBout,1250);
   }
 };

 const recoverCombatReplay=(error)=>{
  if(replayFinished)return;
  replayFinished=true;
  console.error('Combat replay recovered after an animation error.',error);
  if (typeof bgmManager !== 'undefined' && bgmManager.restore) bgmManager.restore();
  try{const output=scene.querySelector('#combatResultOutput');if(output){output.innerHTML=resultHtml||'<div class="combat-result-card">The fight result has been recorded.</div>';output.classList.add('show');}}catch(_){}
  const a=document.getElementById('leagueBoutBtn'),b=document.getElementById('champFightBtn'),c=document.getElementById('cupFightButton');
  if(a)a.disabled=false;if(b)b.disabled=false;if(c)c.disabled=false;combatAnimationBusy=false;
  if(legendFightButton){const legendASelect=document.getElementById('legendA'),legendBSelect=document.getElementById('legendB');legendFightButton.disabled=!legendASelect||!legendBSelect||!legendASelect.value||!legendBSelect.value||legendASelect.value===legendBSelect.value;}
  if(typeof onComplete==='function'){const callback=onComplete;onComplete=null;try{callback();}catch(callbackError){console.error('Post-fight update failed.',callbackError);}}
 };
 const safeUpdateStage=()=>{if(replayFinished)return;try{updateStage();}catch(error){recoverCombatReplay(error);}};
 const a=document.getElementById('leagueBoutBtn'),b=document.getElementById('champFightBtn'),c=document.getElementById('cupFightButton');
 if(a)a.disabled=true;if(b)b.disabled=true;if(c)c.disabled=true;if(legendFightButton)legendFightButton.disabled=true;
 window.setTimeout(safeUpdateStage,350);
}

"""
    new_content = content[:start_idx] + new_fn + content[end_idx:]
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("Conditional V3 Mortal Kombat Finisher successfully wired into playPlayerCombatAnimation!")

if __name__ == "__main__":
    main()
