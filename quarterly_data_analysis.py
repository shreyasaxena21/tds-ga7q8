"""
Quarterly Data Analysis - Q2 2025 Performance Review
Author: 22f1000662@ds.study.iitm.ac.in
Date: August 17, 2025

This script analyzes quarterly performance metrics and generates visualizations
to understand trends, benchmark comparisons, and provide business recommendations.

Generated with LLM/AI assistance for advanced data analysis and visualization.
LLM Reference: https://chatgpt.com/codex/tasks
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducible results
np.random.seed(42)

def generate_quarterly_data():
    """Generate synthetic quarterly data for analysis"""
    quarters = ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024', 'Q1 2025', 'Q2 2025']
    
    # Generate data with declining trend that needs improvement
    base_values = [8.2, 7.8, 7.1, 6.9, 6.5, 6.1]
    performance_metrics = []
    
    for i, quarter in enumerate(quarters):
        # Add some realistic variance
        actual_value = base_values[i] + np.random.normal(0, 0.15)
        performance_metrics.append({
            'quarter': quarter,
            'performance_score': max(4.0, actual_value),  # Ensure minimum reasonable value
            'benchmark': 15.0,  # Target benchmark
            'market_share': max(12, 18 - i * 0.8 + np.random.normal(0, 0.5)),
            'customer_satisfaction': max(70, 85 - i * 2 + np.random.normal(0, 2)),
            'revenue_millions': max(50, 80 - i * 4 + np.random.normal(0, 3))
        })
    
    return pd.DataFrame(performance_metrics)

def calculate_statistics(df):
    """Calculate key statistics from the data"""
    current_avg = df['performance_score'].mean()
    latest_score = df['performance_score'].iloc[-1]
    target = 15.0
    gap_to_target = target - latest_score
    trend_slope = np.polyfit(range(len(df)), df['performance_score'], 1)[0]
    
    return {
        'current_average': current_avg,
        'latest_score': latest_score,
        'target': target,
        'gap_to_target': gap_to_target,
        'trend_slope': trend_slope,
        'declining_trend': trend_slope < 0
    }

def create_visualizations(df, stats):
    """Create comprehensive visualizations for the analysis"""
    
    # Set style
    plt.style.use('default')
    sns.set_palette("husl")
    
    # Create subplot figure
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Quarterly Performance Analysis - Q2 2025 Review', 
                 fontsize=16, fontweight='bold', y=0.98)
    
    # 1. Performance Score Trend
    ax1 = axes[0, 0]
    quarters_numeric = range(len(df))
    ax1.plot(quarters_numeric, df['performance_score'], 'o-', linewidth=3, markersize=8, 
             label='Actual Performance', color='#e74c3c')
    ax1.axhline(y=stats['target'], color='#27ae60', linestyle='--', linewidth=2, 
                label=f'Target: {stats["target"]}')
    ax1.fill_between(quarters_numeric, df['performance_score'], stats['target'], 
                     alpha=0.3, color='#e74c3c')
    
    ax1.set_title('Performance Score Trend vs Target', fontweight='bold')
    ax1.set_xlabel('Quarter')
    ax1.set_ylabel('Performance Score')
    ax1.set_xticks(quarters_numeric)
    ax1.set_xticklabels(df['quarter'], rotation=45)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Add trend line
    z = np.polyfit(quarters_numeric, df['performance_score'], 1)
    p = np.poly1d(z)
    ax1.plot(quarters_numeric, p(quarters_numeric), "--", alpha=0.8, color='#34495e', 
             label='Trend Line')
    
    # 2. Gap Analysis
    ax2 = axes[0, 1]
    gaps = [stats['target'] - score for score in df['performance_score']]
    colors = ['#e74c3c' if gap > 0 else '#27ae60' for gap in gaps]
    
    bars = ax2.bar(range(len(df)), gaps, color=colors, alpha=0.7)
    ax2.set_title('Gap to Target Analysis', fontweight='bold')
    ax2.set_xlabel('Quarter')
    ax2.set_ylabel('Gap to Target (15.0)')
    ax2.set_xticks(range(len(df)))
    ax2.set_xticklabels(df['quarter'], rotation=45)
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=1)
    ax2.grid(True, alpha=0.3)
    
    # Add value labels on bars
    for bar, gap in zip(bars, gaps):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.1 if height > 0 else height - 0.3,
                f'{gap:.1f}', ha='center', va='bottom' if height > 0 else 'top', fontweight='bold')
    
    # 3. Multi-metric Comparison
    ax3 = axes[1, 0]
    
    # Normalize metrics for comparison (0-100 scale)
    normalized_performance = (df['performance_score'] / stats['target']) * 100
    normalized_satisfaction = df['customer_satisfaction']
    normalized_market = (df['market_share'] / 20) * 100  # Assuming 20% is good market share
    
    x = range(len(df))
    width = 0.25
    
    ax3.bar([i - width for i in x], normalized_performance, width, 
            label='Performance Score', alpha=0.8, color='#e74c3c')
    ax3.bar(x, normalized_satisfaction, width, 
            label='Customer Satisfaction', alpha=0.8, color='#3498db')
    ax3.bar([i + width for i in x], normalized_market, width, 
            label='Market Share', alpha=0.8, color='#f39c12')
    
    ax3.set_title('Multi-Metric Performance Comparison', fontweight='bold')
    ax3.set_xlabel('Quarter')
    ax3.set_ylabel('Normalized Score (0-100)')
    ax3.set_xticks(x)
    ax3.set_xticklabels(df['quarter'], rotation=45)
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # 4. Revenue Impact Analysis
    ax4 = axes[1, 1]
    
    # Create correlation between performance and revenue
    ax4.scatter(df['performance_score'], df['revenue_millions'], 
               s=100, alpha=0.7, color='#9b59b6')
    
    # Add trend line
    z = np.polyfit(df['performance_score'], df['revenue_millions'], 1)
    p = np.poly1d(z)
    x_trend = np.linspace(df['performance_score'].min(), df['performance_score'].max(), 100)
    ax4.plot(x_trend, p(x_trend), "--", alpha=0.8, color='#e74c3c', linewidth=2)
    
    ax4.set_title('Performance vs Revenue Correlation', fontweight='bold')
    ax4.set_xlabel('Performance Score')
    ax4.set_ylabel('Revenue (Millions USD)')
    ax4.grid(True, alpha=0.3)
    
    # Add correlation coefficient
    corr_coef = np.corrcoef(df['performance_score'], df['revenue_millions'])[0, 1]
    ax4.text(0.05, 0.95, f'Correlation: {corr_coef:.3f}', 
             transform=ax4.transAxes, fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('quarterly_analysis_dashboard.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    
    return fig

def generate_recommendations(stats):
    """Generate business recommendations based on analysis"""
    recommendations = []
    
    if stats['declining_trend']:
        recommendations.append({
            'priority': 'HIGH',
            'category': 'Market Strategy',
            'recommendation': 'Expand into new market segments',
            'rationale': f'Current declining trend ({stats["trend_slope"]:.3f} per quarter) requires immediate market expansion to reverse negative trajectory.',
            'expected_impact': 'Target +3-5 point improvement in performance score',
            'timeline': '6-9 months'
        })
    
    recommendations.extend([
        {
            'priority': 'HIGH',
            'category': 'Product Innovation',
            'recommendation': 'Accelerate new product development',
            'rationale': f'Gap of {stats["gap_to_target"]:.1f} points to target requires significant innovation.',
            'expected_impact': 'Target +2-3 point improvement',
            'timeline': '3-6 months'
        },
        {
            'priority': 'MEDIUM',
            'category': 'Customer Experience',
            'recommendation': 'Implement customer retention programs',
            'rationale': 'Improve customer satisfaction to drive performance metrics.',
            'expected_impact': 'Target +1-2 point improvement',
            'timeline': '2-4 months'
        },
        {
            'priority': 'MEDIUM',
            'category': 'Operational Excellence',
            'recommendation': 'Optimize operational processes',
            'rationale': 'Streamline operations to improve efficiency and performance.',
            'expected_impact': 'Target +1 point improvement',
            'timeline': '4-8 months'
        }
    ])
    
    return recommendations

def main():
    """Main analysis function"""
    print("🔍 Quarterly Data Analysis - Q2 2025")
    print("=" * 50)
    print(f"📧 Analysis by: 22f1000662@ds.study.iitm.ac.in")
    print(f"📅 Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Generate and analyze data
    df = generate_quarterly_data()
    stats = calculate_statistics(df)
    
    # Display key findings
    print("📊 KEY FINDINGS")
    print("-" * 30)
    print(f"Current Average Performance: {stats['current_average']:.2f}")
    print(f"Latest Quarter Score: {stats['latest_score']:.2f}")
    print(f"Target Score: {stats['target']:.2f}")
    print(f"Gap to Target: {stats['gap_to_target']:.2f}")
    print(f"Trend Direction: {'📉 Declining' if stats['declining_trend'] else '📈 Improving'}")
    print()
    
    # Create visualizations
    print("📈 Generating visualizations...")
    fig = create_visualizations(df, stats)
    print("✅ Dashboard saved as 'quarterly_analysis_dashboard.png'")
    
    # Generate recommendations
    recommendations = generate_recommendations(stats)
    
    print("\n🎯 TOP RECOMMENDATIONS")
    print("-" * 30)
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. [{rec['priority']}] {rec['recommendation']}")
        print(f"   Category: {rec['category']}")
        print(f"   Expected Impact: {rec['expected_impact']}")
        print(f"   Timeline: {rec['timeline']}")
        print()
    
    # Save data and results
    df.to_csv('quarterly_data.csv', index=False)
    print("✅ Data saved as 'quarterly_data.csv'")
    
    return df, stats, recommendations

if __name__ == "__main__":
    df, stats, recommendations = main()
