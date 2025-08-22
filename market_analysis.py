"""
Market Segment Analysis - Supporting Analysis
Author: 22f1000662@ds.study.iitm.ac.in

This module provides detailed market segmentation analysis to support 
the primary recommendation of expanding into new market segments.

Generated with LLM/AI assistance for comprehensive market analysis.
LLM Reference: https://chatgpt.com/codex/tasks
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_market_segments():
    """Analyze potential market segments for expansion"""
    
    # Market segment opportunity analysis
    segments = {
        'Segment': ['Enterprise SaaS', 'Small Business', 'International', 'Mobile-First', 'Industry Vertical'],
        'Market_Size_Millions': [250, 180, 320, 200, 150],
        'Competition_Level': [3, 4, 2, 5, 3],  # 1-5 scale
        'Entry_Difficulty': [4, 2, 5, 3, 4],   # 1-5 scale
        'Expected_ROI': [8.5, 6.2, 9.1, 7.8, 8.0],
        'Time_to_Market_Months': [6, 3, 9, 4, 7],
        'Projected_Performance_Impact': [4.2, 2.8, 4.8, 3.5, 3.9]
    }
    
    df_segments = pd.DataFrame(segments)
    
    # Calculate opportunity score
    df_segments['Opportunity_Score'] = (
        (df_segments['Market_Size_Millions'] / 100) * 0.3 +
        (6 - df_segments['Competition_Level']) * 0.2 +
        (6 - df_segments['Entry_Difficulty']) * 0.1 +
        df_segments['Expected_ROI'] * 0.2 +
        (12 - df_segments['Time_to_Market_Months']) * 0.1 +
        df_segments['Projected_Performance_Impact'] * 0.1
    )
    
    return df_segments.sort_values('Opportunity_Score', ascending=False)

def create_segment_visualization():
    """Create market segment opportunity visualization"""
    
    df = analyze_market_segments()
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Market Segment Expansion Analysis', fontsize=16, fontweight='bold')
    
    # 1. Opportunity Score Ranking
    ax1 = axes[0, 0]
    bars = ax1.barh(df['Segment'], df['Opportunity_Score'], color='skyblue', alpha=0.8)
    ax1.set_title('Market Segment Opportunity Ranking', fontweight='bold')
    ax1.set_xlabel('Opportunity Score')
    
    # Add value labels
    for bar in bars:
        width = bar.get_width()
        ax1.text(width + 0.1, bar.get_y() + bar.get_height()/2, 
                f'{width:.1f}', ha='left', va='center', fontweight='bold')
    
    # 2. Market Size vs Performance Impact
    ax2 = axes[0, 1]
    scatter = ax2.scatter(df['Market_Size_Millions'], df['Projected_Performance_Impact'], 
                         s=df['Expected_ROI']*30, alpha=0.7, c=df['Opportunity_Score'], 
                         cmap='viridis')
    ax2.set_title('Market Size vs Performance Impact', fontweight='bold')
    ax2.set_xlabel('Market Size (Millions USD)')
    ax2.set_ylabel('Projected Performance Impact')
    
    # Add segment labels
    for i, segment in enumerate(df['Segment']):
        ax2.annotate(segment, (df['Market_Size_Millions'].iloc[i], 
                              df['Projected_Performance_Impact'].iloc[i]),
                    xytext=(5, 5), textcoords='offset points', fontsize=9)
    
    plt.colorbar(scatter, ax=ax2, label='Opportunity Score')
    
    # 3. Competition vs Entry Difficulty
    ax3 = axes[1, 0]
    bubble_sizes = df['Market_Size_Millions'] / 5
    colors = ['red' if score < 5 else 'orange' if score < 7 else 'green' 
              for score in df['Opportunity_Score']]
    
    ax3.scatter(df['Competition_Level'], df['Entry_Difficulty'], 
               s=bubble_sizes, alpha=0.7, c=colors)
    ax3.set_title('Competition vs Entry Difficulty Analysis', fontweight='bold')
    ax3.set_xlabel('Competition Level (1=Low, 5=High)')
    ax3.set_ylabel('Entry Difficulty (1=Easy, 5=Hard)')
    ax3.grid(True, alpha=0.3)
    
    # Add quadrant labels
    ax3.text(1.5, 4.5, 'Low Competition\nHigh Difficulty', ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.7))
    ax3.text(4.5, 1.5, 'High Competition\nLow Difficulty', ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightcoral", alpha=0.7))
    
    # 4. Timeline vs ROI Analysis
    ax4 = axes[1, 1]
    colors_roi = ['red' if roi < 7 else 'orange' if roi < 8 else 'green' 
                  for roi in df['Expected_ROI']]
    
    bars = ax4.bar(df['Segment'], df['Time_to_Market_Months'], 
                   color=colors_roi, alpha=0.7)
    ax4.set_title('Time to Market Analysis', fontweight='bold')
    ax4.set_ylabel('Time to Market (Months)')
    ax4.set_xticklabels(df['Segment'], rotation=45, ha='right')
    
    # Add ROI labels on bars
    for i, (bar, roi) in enumerate(zip(bars, df['Expected_ROI'])):
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'ROI: {roi:.1f}%', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('market_segment_analysis.png', dpi=300, bbox_inches='tight')
    
    return fig

if __name__ == "__main__":
    print("🎯 Market Segment Analysis")
    print("=" * 40)
    print(f"📧 Analysis by: 22f1000662@ds.study.iitm.ac.in")
    
    df = analyze_market_segments()
    
    print("\n📊 TOP MARKET OPPORTUNITIES")
    print("-" * 30)
    for i, row in df.head(3).iterrows():
        print(f"{i+1}. {row['Segment']}")
        print(f"   Opportunity Score: {row['Opportunity_Score']:.1f}")
        print(f"   Market Size: ${row['Market_Size_Millions']}M")
        print(f"   Performance Impact: +{row['Projected_Performance_Impact']:.1f}")
        print(f"   Expected ROI: {row['Expected_ROI']:.1f}%")
        print(f"   Time to Market: {row['Time_to_Market_Months']} months")
        print()
    
    # Save analysis
    df.to_csv('market_segments_analysis.csv', index=False)
    print("✅ Market segment data saved as 'market_segments_analysis.csv'")
    
    # Create visualizations
    create_segment_visualization()
    print("✅ Market analysis charts saved as 'market_segment_analysis.png'")
