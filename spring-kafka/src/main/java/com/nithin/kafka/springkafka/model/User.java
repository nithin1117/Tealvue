package com.nithin.kafka.springkafka.model;

public class User {

    private String symbol;
    private double open;
    private double high;
    private double low;
    private double close;
    private double oi;
    private int vol;



    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public double getOpen() {
        return open;
    }

    public void setOpen(double open) {
        this.open = open;
    }

    public double getHigh() {
        return high;
    }

    public void setHigh(double high) {
        this.high = high;
    }

    public double getLow() {
        return low;
    }

    public void setLow(double low) {
        this.low = low;
    }

    public double getClose() {
        return close;
    }

    public void setClose(double close) {
        this.close = close;
    }

    public double getOi() {
        return oi;
    }

    public void setOi(double oi) {
        this.oi = oi;
    }

    public int getVol() {
        return vol;
    }

    public void setVol(int vol) {
        this.vol = vol;
    }

    public User() {
    }

    public User(String symbol, double open, double high, double low, double close, double oi, int vol) {

        this.symbol = symbol;
        this.open = open;
        this.high = high;
        this.low = low;
        this.close = close;
        this.oi = oi;
        this.vol = vol;
    }

    @Override
    public String toString() {
        final StringBuffer sb = new StringBuffer("User{");
        sb.append("symbol='").append(symbol).append('\'');
        sb.append(", open='").append(open).append('\'');
        // sb.append(", high='").append(open).append('\'');
        // sb.append(", low='").append(open).append('\'');
        // sb.append(", close='").append(open).append('\'');
        sb.append('}');
        return sb.toString();
    }
} 