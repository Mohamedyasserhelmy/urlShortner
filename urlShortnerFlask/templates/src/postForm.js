import React, { Component } from 'react';

class postForm extends Component {
  render() {
    return (
      <form>
        {
            <input type="text" name="web" required/>
            <input type="text" name="android_primary" required/>
            <input type="text" name="android_fallback" required/>
            <input type="text" name="ios_primary" required/>
            <input type="text" name="ios_fallback"  required/>
        }
      </form>
    );
  }
}

export default postForm;